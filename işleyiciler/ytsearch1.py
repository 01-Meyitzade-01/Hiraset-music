# günlüğe kaydetme şeyleri
ithalat  günlüğü

dan  pyrogram . türleri  içe aktarma  Mesajı
dan  search_engine_parser  ithalat  Google Arama
dan  youtube_search  ithalat  YoutubeSearch

dan  pyrogram  ithalat  Client  olarak  uygulaması , filtreler

günlüğe kaydetme . temelYapılandırma (
    seviye = günlüğe kaydetme . DEBUG , format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
kaydedici  =  günlüğe kaydetme . getLogger ( __name__ )

 pirogramı içe aktar

günlüğe kaydetme . getLogger ( "pirogram" ). setLevel ( günlüğe kaydetme . UYARI )

@ uygulama . on_message ( pirogram . filtreler . komut ([ "ara" ]))
zaman uyumsuz  def  ytara ( _ , mesaj : Mesaj ):
    dene :
        if  len ( mesaj . komut ) <  2 :
             mesaj bekliyoruz . answer_text ( "/ search'ün bir argümana ihtiyacı var!" )
            dönüş
        sorgu  =  mesaj . metin . böl ( Yok , 1 )[ 1 ]
        m  =  mesaj bekliyor  . answer_text ( "kaynaklardan bağlantı bulunuyor...." )
        sonuçlar  =  YoutubeArama ( sorgu , max_results = 4 ). to_dict ()
        ben  =  0
        metin  =  ""
         ben  <  4 iken :
            metin  +=  f"Başlık - { sonuçlar [ i ][ 'başlık' ] } \n "
            metin  +=  f"Süre - { sonuçlar [ i ][ 'süre' ] } \n "
            text  +=  f"Görünümler - { sonuçlar [ i ][ 'görünümler' ] } \n "
            metin  +=  f"Kanal - { sonuçlar [ i ][ 'kanal' ] } \n "
            metin  +=  f"https://youtube.com { sonuçlar [ i ][ 'url_suffix' ] } \n \n "
            ben  +=  1
        beklemek  m . düzenle ( metin , disable_web_page_preview = True )
     e olarak İstisna  hariç : 
         mesaj bekliyoruz . answer_text ( str ( e ))