# 1
def create_phone_number(number_list):
    all_check = 1
    alpha_check = 0
    for i in number_list: 
        if i.isalpha() == True:
            alpha_check += 0
        else:
            alpha_check += 1
    # print(alpha_check)
    if alpha_check != len(number_list):
        print('Invalid input. No Alphabet')
        all_check *= 0
    else:
        all_check *= 1
    
    if len(number_list) != 10:
        print('Digits must be in length of 10, not more or less.')
        all_check *= 0
    else:
        all_check *= 1
    
    positive_check = 0
    for i in number_list:
        if i == '-':
            positive_check += 0
        else:
            positive_check += 1
    if positive_check != len(number_list):
        print('Input only positive number.')
        all_check *= 0
    else:
        all_check *= 1

    symbols_check = 0
    for i in number_list:
        if i.isalnum() == False:
            symbols_check += 0
        else:
            symbols_check += 1
    if symbols_check != len(number_list):
        print('Invalid Input. No symbols.')
        all_check *= 0
    else:
        all_check *= 1    
    
    if all_check == 1:
        print(f'({number_list[0:3]}) {number_list[3:6]}-{number_list[6:10]}')
number_list = input('Input your phone number: ')
create_phone_number(number_list)

# 2
def move_zeros(list_input):
    result_list = []
    for i in list_input:
        if i == 0:
            result_list.append(i)
        else:
            result_list.insert(0, i)
    
    zero_count = result_list.count(0)
    print(zero_count)
    end_cut = len(result_list)-zero_count-1
    print(end_cut)
    result_list_without_zero_inversed = result_list[end_cut::-1]
    print(result_list_without_zero_inversed)
    
    i = 1
    while i <= zero_count:
        result_list_without_zero_inversed.append(0)
        i+=1

    print(f'result: {result_list_without_zero_inversed}')
    # print(f'result: {result_list}' )

list_input = [1,2,3,0,7,'False','a',0,'Nanimo','YAYA',0,'d','z']
move_zeros(list_input)

# 3
class Statistic:
    def __init__(self, list_angka):
        self.list_angka = list_angka
        
    def mean(self, list_angka): # Rata2
        i = self.list_angka[0]
        j = 1
        while j <= len(self.list_angka)-1:
            i += self.list_angka[j]
            j += 1
        print(f'Mean = {i/len(self.list_angka)}')
        self.mean = i/len(self.list_angka)
        return(self.mean)
        
    def median(self, list_angka): # Nilai tengah
        self.list_angka.sort()
        # print(self.list_angka)

        panjang_list_angka = len(self.list_angka)

        if (panjang_list_angka % 2) == 2:
            median = (self.list_angka[panjang_list_angka/2]+self.list_angka[panjang_list_angka/2+1])/2
            print(f'Median = {median}')
        else:
            import math as m
            median = self.list_angka[m.ceil(panjang_list_angka/2)]
            print(f'Median = {median}')    

    def mode(self, list_angka): # Nilai terbanyak. Jika frekuensi angka muncul ada yg sama, maka 'tidak ada modus'.
        # set_list_angka = set(self.list_angka)
        # list_set_list_angka = list(set_list_angka)
        self.list_angka.sort()
        
        set_list_angka = set(self.list_angka)

        list_set_list_angka = list(set_list_angka)

        jumlah_angka = []
        for i in list_set_list_angka:
            a = self.list_angka.count(i)
            jumlah_angka.append(a)
        # print(jumlah_angka)
        # if len(set_list_angka) % 3:
        # print(list_set_list_angka)

        maksimum = 0    
        for i in jumlah_angka:
            if i > maksimum:
                maksimum = i
        # print(maksimum)

        jumlah_angka_maksimum = jumlah_angka.count(maksimum)

        if jumlah_angka_maksimum > 1:
            print('Tidak ada modus')
        else:
            print(f'Modus = {list_set_list_angka[jumlah_angka.index(maksimum)]}')

    def std(self, list_angka): # Standard deviasi
        import math as m
        for i in self.list_angka:
            z = (i-self.mean)**2
        # print(z)

        standrad_deviasi = m.sqrt(z/len(self.list_angka))
        print(f'Standard deviasi = {standrad_deviasi}')

list_angka = [1,2,3,4,5,6,5,9,4,4]

numeric_check = 0
for i in list_angka:
    if isinstance(i, int) == True:
        numeric_check += 1
    else:
        numeric_check += 0

if numeric_check != len(list_angka):
    print('Invalid Input! All values must be Integer')
else:
    pass

st = Statistic(list_angka)
st.mean(list_angka)
st.median(list_angka)
st.mode(list_angka)
st.std(list_angka)