""" 
AMAÇ:

Derste işlenen konuların pekiştirilmesi.



ÖDEV TANIMI:

Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
"""

students = []

def add_student(name):
    students.append(name.capitalize())
    print(name.capitalize() + " listeye eklendi.")
    
def remove_student(name):
    if name in students:
        students.remove(name)
        print(name.capitalize() + " listeden silindi.")
    else:
        print(name.capitalize() + " listede yok.")
        
def add_multiple_students(names):
    while True:
        name = input("Eklemek istediğiniz öğrencinin adını giriniz(Çıkış yapmak için q tuşuna basınız.): ")
        if name == "q":
            break
        else:
            names.append(name.capitalize())
            print(name.capitalize() + " listeye eklendi.")

def remove_multiple_students():
    while True:
        name = input("Silmek istediğiniz öğrencinin adını giriniz(Çıkış yapmak için q tuşuna basınız.): ")
        if name == "q":
            break
        else:
            remove_student(name)

def info():
    for student in students:
        print(student.capitalize())


def student_no(student):
    if student in students:
        no = students.index(student) + 1
        print(student.capitalize() + " öğrencisinin numarası: " + str(no))
    else:
        print(student.capitalize() + " listede yok.")