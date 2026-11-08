#!/usr/bin/env python3
"""
Automated TDD verification suite for the Animal Scrypt Stage-1 Kernel (skeleton/interfaces.py).
Tests the MVP done-conditions defined in /seed/00-context.md:
1. Persistent companion identity & biography (authored_lore)
2. Explicit memory approval state machine (PROPOSED -> APPROVED -> DELETED)
3. Persistence of >= 3 approved memories across a database/application restart
4. Bilateral memory fragment exchange & revocation
5. Portable identity & ownership bundle export
"""

import pathlib
import tempfile
import unittest

from skeleton.interfaces import AnimalScryptKernel, ChassisSpec


class TestAnimalScryptKernel(unittest.TestCase):
    def test_seven_day_memory_survives_application_restart(self) -> None:
        """MVP Done-Condition #2, #3, #5: Creature recalls >= 3 approved details after app restart."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_file = str(pathlib.Path(tmpdir) / "animal_scrypt_test.db")

            # Session 1 (Day 1): Register creature, propose 4 memories, approve 3, reject 1
            kernel_day1 = AnimalScryptKernel(db_path=db_file)
            kernel_day1.register_companion(
                companion_id="mk-01-scad",
                owner_id="kj_cornish",
                name="BOLT-01 (Studio Engineer)",
                authored_lore="3D-printed engineer creature fabricated in Savannah.",
                chassis=ChassisSpec(),
            )

            m1 = kernel_day1.propose_memory("mk-01-scad", "project", "Wall thickness set to 2.4mm in OpenSCAD.")
            m2 = kernel_day1.propose_memory("mk-01-scad", "routine", "Print bed leveled with 0.2mm nozzle offset.")
            m3 = kernel_day1.propose_memory("mk-01-scad", "observation", "NTAG215 sticker recesses into 28mm base slot.")
            m4_noise = kernel_day1.propose_memory("mk-01-scad", "interest", "Unapproved chat noise that must not persist.")

            kernel_day1.review_memory(m1, approve=True)
            kernel_day1.review_memory(m2, approve=True)
            kernel_day1.review_memory(m3, approve=True)
            kernel_day1.review_memory(m4_noise, approve=False)
            kernel_day1.conn.close()

            # Simulate application restart (Day 7)
            kernel_day7 = AnimalScryptKernel(db_path=db_file)
            bundle = kernel_day7.export_portable_bundle("mk-01-scad")

            self.assertEqual(bundle["companion_manifest"]["owner_id"], "kj_cornish")
            self.assertEqual(bundle["companion_manifest"]["name"], "BOLT-01 (Studio Engineer)")
            approved_texts = [m["content"] for m in bundle["approved_private_memories"]]
            self.assertEqual(len(approved_texts), 3)
            self.assertIn("Wall thickness set to 2.4mm in OpenSCAD.", approved_texts)
            self.assertIn("Print bed leveled with 0.2mm nozzle offset.", approved_texts)
            self.assertIn("NTAG215 sticker recesses into 28mm base slot.", approved_texts)
            self.assertNotIn("Unapproved chat noise that must not persist.", approved_texts)
            kernel_day7.conn.close()

    def test_unapproved_memory_cannot_be_exchanged(self) -> None:
        """Only user-APPROVED memories can be shared or forked."""
        kernel = AnimalScryptKernel()
        self.addCleanup(kernel.conn.close)
        kernel.register_companion("c1", "u1", "Parent Animal", "Lore 1")
        kernel.register_companion("c2", "u2", "Child Animal", "Lore 2")
        unapproved_id = kernel.propose_memory("c1", "project", "Draft spec")

        with self.assertRaises(PermissionError):
            kernel.propose_fragment_exchange(unapproved_id, "c1", "c2", "Summary")

    def test_ritual_object_requires_parallel_presence(self) -> None:
        """Shared ritual object only advances when all paired participants check in."""
        kernel = AnimalScryptKernel()
        self.addCleanup(kernel.conn.close)
        kernel.create_ritual_object("r1", "Studio Core #1", ["c1", "c2"])

        with self.assertRaises(PermissionError):
            kernel.tend_ritual_object("r1", ["c1"], "Solo attempt")

        updated = kernel.tend_ritual_object("r1", ["c1", "c2"], "Parallel studio sprint")
        self.assertEqual(updated["state"], "RESONATING")
        self.assertEqual(updated["vitality_points"], 1)

    def test_simulated_royalty_rule_demonstration(self) -> None:
        """MVP Done-Condition #6: Simulated creator-to-owner transfer records a 20% parent royalty allocation in test ledger."""
        kernel = AnimalScryptKernel()
        self.addCleanup(kernel.conn.close)
        kernel.register_companion("parent-mk-01", "creator_kj", "ORIGIN-01 (Parent Blueprint)", "Original studio parent.")
        kernel.register_companion("child-mk-02", "buyer_savannah", "FORK-02 (Child Shell)", "Forked from ORIGIN-01.")

        tx = kernel.record_royalty_transfer(
            parent_companion_id="parent-mk-01",
            child_companion_id="child-mk-02",
            creator_id="creator_kj",
            buyer_id="buyer_savannah",
            gross_amount_cents=1500,
        )
        self.assertEqual(tx["gross_amount_cents"], 1500)
        self.assertEqual(tx["creator_royalty_cents"], 300)  # 20% to parent creator
        self.assertEqual(tx["platform_fee_cents"], 150)     # 10% platform fee
        self.assertEqual(tx["net_settlement_cents"], 1050)  # 70% net
        self.assertEqual(tx["settlement_mode"], "SIMULATED_TEST_LEDGER")

        bundle = kernel.export_portable_bundle("parent-mk-01")
        self.assertEqual(len(bundle["royalty_ledger"]), 1)
        self.assertEqual(bundle["royalty_ledger"][0]["child_companion_id"], "child-mk-02")


if __name__ == "__main__":
    unittest.main()
