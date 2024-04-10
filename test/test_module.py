from unittest import TestCase, main
from module import volume_esfera


class ResolucaoEmDOT(TestCase):
    def test_volume_esfera(self):
        self.assertEqual(volume_esfera(5), 523.59)
        self.assertEqual(volume_esfera(10), 4188.79)
        self.assertEqual(volume_esfera(1), 4.18)
        self.assertEqual(volume_esfera(0), 0)
        self.assertEqual(volume_esfera(-2), -33.51)
        self.assertEqual(volume_esfera(3.14), 129.68)
        self.assertIsInstance(volume_esfera(6), float)

    def test_media_escolar(self):
        pass

    def test_eh_primo(self):
        pass

    def test_tempo_processo(self):
        pass

    def test_converte_idade_em_dias(self):
        pass


if __name__ == "__main__":
    main()
