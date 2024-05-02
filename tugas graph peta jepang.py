class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
    
print("petajepang")
petajepang = Peta()
#menambahkan kota baru
petajepang.tambahkanKota("osaka")
petajepang.tambahkanKota("hiagashiosaka")
petajepang.tambahkanKota("yao osaka")
petajepang.tambahkanKota("matsubara")
petajepang.tambahkanKota("sakai")
petajepang.tambahkanKota("moriguchi")
petajepang.tambahkanKota("kadoma")
petajepang.tambahkanKota("daito")
petajepang.tambahkanKota("settsu")
petajepang.tambahkanKota("suita")
print('----------------------------------------------')
#menghubungkan kota dengan jalan atau vertex dengan edge
petajepang.tambahkanJalan("osaka","hiagashiosaka")
petajepang.tambahkanJalan("yao osaka","matsubara")
petajepang.tambahkanJalan("sakai","moriguchi")
petajepang.tambahkanJalan("kadoma","daito")
petajepang.tambahkanJalan("daito","settsu ")
petajepang.tambahkanJalan("osaka","yao osaka")
petajepang.tambahkanJalan("osaka","suita")
petajepang.tambahkanJalan("osaka","sakai")
petajepang.tambahkanJalan("osaka","kadoma")
petajepang.tambahkanJalan("osaka","hiagshiosakai")
petajepang.tambahkanJalan("matsubara","sakai")
petajepang.tambahkanJalan("matsubara","moriguchi")
petajepang.tambahkanJalan("matsubara","settsu")
petajepang.tambahkanJalan("moriguchi","suita")
petajepang.tambahkanJalan("moriguchi","sakai")
petajepang.tambahkanJalan("moriguchi","settsu")
petajepang.tambahkanJalan("moriguchi","daito")
petajepang.tambahkanJalan("hiagashiosakai","daito")
petajepang.tambahkanJalan("hiagashiosakai","moriguchi")
petajepang.tambahkanJalan("hiagashiosakai","sakai")
petajepang.tambahkanJalan("sakai","settsu")
petajepang.tambahkanJalan("sakai","yao osaka")
petajepang.tambahkanJalan("kadoma","daito")
petajepang.tambahkanJalan("daito","yao osaka")
petajepang.tambahkanJalan("settsu","moriguchi")
petajepang.tambahkanJalan("settsu","suita")
petajepang.tambahkanJalan("settsu","kadoma")
petajepang.tambahkanJalan("moriguchi","hiagshiosakai")
petajepang.tambahkanJalan("osaka","mariguchi")



#menampilkan hasi dari diatas
print('------------OUTPUT AWAL-------------------')
petajepang.printPeta()
print('--------------------Output setalah kota dihapus----------------------')
petajepang.hapusKota("daito")
petajepang.printPeta()
print('------------------------output setelah menghapus jalan-----------------------------')
petajepang.hapusJalan("osaka","suita")
petajepang.printPeta()





