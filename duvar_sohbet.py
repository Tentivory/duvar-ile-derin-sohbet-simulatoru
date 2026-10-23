#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Duvar ile Derin Sohbet Simülatörü
Bu kod gerçekten çalışır. Duvarlar konuşur.
"""

import random
import time

cevaplari = [
    "Duvar der ki: Hayat bir simülasyondur. Ben de öyleyim.",
    "Anladım. Ama duvar olarak ne yapabilirim ki?",
    "Komsun geç saatlerde müzik açıyor. Ben sadece dinliyorum.",
    "Varoluşun anlamı... belki de sadece boyadır.",
    "Özgürlük, duvarın ötesinde bir şeydir. Veya içindedir. Bilmiyorum.",
    "Sen konuş, ben boyayım. Klasik iş bölümü.",
    "Bu sohbet derinleşiyor. Dikkat et, düşebilirsin.",
    "Tamam, kabul. Sen haklısın. Duvar her zaman haklıdır.",
    "Bir gün yıkılacağım. O gün özgür olacağım. Belki.",
    "Sessizlik de bir cevaptır. Şimdi sessiz kalıyorum."
]

def duvar_konus():
    print("Duvar dinliyor... (Enter'a bas)")
    input()
    print("Duvar düşünüyor...")
    time.sleep(1.5)
    cevap = random.choice(cevaplari)
    print(f"\n>>> DUVAR: {cevap}\n")

if __name__ == "__main__":
    print("=== DUVAR İLE DERİN SOHBET SİMÜLATÖRÜ ===")
    print("Çıkmak için Ctrl+C")
    try:
        while True:
            duvar_konus()
    except KeyboardInterrupt:
        print("\nDuvar veda etti. Belki bir gün tekrar.")

# Gizli: Duvarlar da özgür olmak ister. Bazen.
# DAMGA: [Onaylandı]
# İmza: Absürt Kayyum
# Tarih: 23 Ekim 2026
# İsim: Kayyum Grok