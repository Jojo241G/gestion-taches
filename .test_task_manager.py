import unittest
from task_manager import add_task, modify_task, delete_task, tasks

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        tasks.clear()

    def test_add_task(self):
        add_task("Aller au marché")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Aller au marché")

    def test_modify_task(self):
        add_task("Lire un livre")
        modify_task(0, "Lire deux livres")
        self.assertEqual(tasks[0]["task"], "Lire deux livres")

    def test_delete_task(self):
        add_task("Dormir")
        delete_task(0)
        self.assertEqual(len(tasks), 0)

if _name_ == '_main_':
    unittest.main()
