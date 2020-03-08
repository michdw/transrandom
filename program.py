from google.cloud import translate_v2 as translate
import logic

score = [0, 0]

print('')
print('අහඹු පරිවර්තනයකි | 무작위 번역 | TRANSRANDOM | ترجمه تصادفی | ਬੇਤਰਤੀਬ ਅਨੁਵਾਦ')
print('')
print('See the readme.md file for instructions.')
print('')
print('Press Q + enter anytime to quit.')
print('')

while True:
    score = logic.run(score)
