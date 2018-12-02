KolvoRaspilov = 0
MassivBreven = []

print("VVEDITE KOLICHESVO BREVEN ot 2 do 1000 i RAZNICU DLINY ot 100 do 1000 CHEREZ PROBEL: ", end="")
KolvoBreven, RaznicaDliny = input().split(" ")
KolvoBreven, RaznicaDliny = int(KolvoBreven), int(RaznicaDliny)

for i in range(0, KolvoBreven):
  print("DLINA BREVNA #" + str(i + 1) + ": ", end="")
  MassivBreven.append(int(input()))
print("SPISOK BREVEN: " + str(MassivBreven))
  
min = MassivBreven[0] #
for i in range(1, KolvoBreven):
  if MassivBreven[i] < min:
    min = MassivBreven[i]
print("SAMOE KOROTKOE BREVNO: " + str(min))

max = min / 2 + RaznicaDliny
print("RAZNICA V DLINE V DIAPAZONE OT " + str(min / 2 - RaznicaDliny) + " DO "+ str(max))

for i in range(0, KolvoBreven):
  temp = MassivBreven[i]
  k = 2
  while (temp > max):
    temp = MassivBreven[i] / k
    k += 1
  if k - 2 == 0:
   k = 3
  print("BREVNO #" + str(i + 1) + ", DLINA CHURBAKA: "+ str(temp) + ", KOLICHESTVO RASPILOV BREVNA: " + str(k - 2))
  KolvoRaspilov += (k - 2)
print("MINIMALNOE KOLICHESTVO RASPILOV VSEH BREVEN: " + str(KolvoRaspilov))
