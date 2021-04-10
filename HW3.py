ogrenci1 =  str(input("1.Öğrenci Adı:"))
midterm1 = int(input("Arasınav Girin: "))
project1 = int(input("proje notu: "))
final1 = int(input("final notu: "))
ortalama1 = 0.3*midterm1 + 0.3*project1 + 0.4*final1

ogrenci2 =  str(input("2.Öğrenci Adı:"))
midterm2 = int(input("Arasınav Girin: "))
project2 = int(input("proje notu: "))
final2 = int(input("final notu: "))
ortalama2 = 0.3*midterm2 + 0.3*project2 + 0.4*final2

ogrenci3 =  str(input("3.Öğrenci Adı:"))
midterm3 = int(input("Arasınav Girin: "))
project3 = int(input("proje notu: "))
final3 = int(input("final notu: "))
ortalama3 = 0.3*midterm1 + 0.3*project3 + 0.4*final3

ogrenci4 =  str(input("4.Öğrenci Adı:"))
midterm4 = int(input("Arasınav Girin: "))
project4 = int(input("proje notu: "))
final4 = int(input("final notu: "))
ortalama4 = 0.3*midterm4 + 0.3*project4 + 0.4*final4

ogrenci5 =  str(input("5.Öğrenci Adı:"))
midterm5 = int(input("Arasınav Girin: "))
project5 = int(input("proje notu: "))
final5 = int(input("final notu: "))
ortalama5 = 0.3*midterm5 + 0.3*project5 + 0.4*final5

dictionary= {"student1" : [ogrenci1, midterm1, project1,final1,ortalama1], 
    "student2" : [ogrenci2, midterm2, project2, final2, ortalama2],
    "student3" : [ogrenci3, midterm3, project3, final3, ortalama3],
    "student4" : [ogrenci4, midterm4, project4, final4, ortalama4],
    "student5" : [ogrenci5, midterm5, project5, final5, ortalama5]}

print(dictionary)

liste = [dictionary["student1"][4], dictionary["student2"][4], 
        dictionary["student3"][4], dictionary["student4"][4], dictionary["student5"][4]]


liste.sort(reverse=True)
print(liste)
