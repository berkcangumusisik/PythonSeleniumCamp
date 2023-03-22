"""  
AMAÇ:

Araştırma yaparak derste işlenen konuların tekrar edilmesi.

ÖDEV TANIMI:

Aşağıdaki konuları araştırıp not alarak notlarınızı arkadaşlarınızla bu ödevin yorum kısmında paylaşınız;

HTML
HTML Locators
Selenium'da aksiyonlar (send_keys, click vb..)
"""

""" 
HTML Nedir?
Hiper Metin İşaretleme Dili (HTML, İngilizce HyperText Markup Language kelimelerinin baş harflerinin kısaltılmasıdır) web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir. 
HTML, bir programlama dili değildir. HTML kodlarıyla kendi başına çalışan bir program yazılamaz. Ancak bu dili yorumlayabilen programlar aracılığıyla çalışabilen programlar yazılabilir.
 Temel gereği yazı, görüntü, video gibi değişik verileri ve bunları içeren sayfaları birbirine basitçe bağlamak, buna ek olarak söz konusu sayfaların web tarayıcısı yazılımları tarafından düzgün olarak görüntülenmesi için gerekli kuralları belirlemektir. HTML kodunu web tarayıcıları okur, yorumlar ve görsel hale dönüştürürler, dolayısıyla aynı HTML kodunun farklı tarayıcılarda farklı sonuç vermesi olasıdır. CSS ve JavaScript ile beraber kullanıldığında HTML vasıtasıyla görsel ve dinamik web siteleri yaratılabilir.
 
 
Html locators
Locators Selenium IDE’ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur. Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur. Site üzerindeki bir elemente örneğin giriş butonuna selenium ile tıklama işlemi yaptırmak istediğimizde bu işlemi locator’lar aracılığıyla yapılır.
•	ID
•	Name
•	ClassName
•	TagName
•	LinkText
•	CssSelector
•	XPath

SELENIUM AKSIYONLAR 
Send_keys(): Input alanlarına vs. Text gönderir
Click () : elementi triggerlamak için kullanılır 
Maximize_window : Erişilen ekranı tam ekran yapar
Set_window_size( , ) : Belirli boyutlarda ekranı ayarlama 
Clear () : text alanını temizler 
Pause () : testin durmasını sağlar 
Back () : önceki sayfaya dönmeyi sağlar 
Forward : İleri sayfaya gitmeyi sağlar 
Refresh (): sayfa yenilemek için kullanılır 
ClickAndHold () : Mouse’ a basılı tutmak 
doubleClick () : Çift tıklamak 
contextClick () : Mouse sağ click 
submit () : formu göndermek için 
Select_by_visible_text() : Görünen texti seçmek 
Find_element_by_xpath() : Elementin xpath yolunu bulur 
Find_element_by_id() : Elementi id’si ile bulmak için 
Find_element_by_name(): Elementi name’i ile bulmak 
Find_element_by_link_text() Web sitesine bağlı olan linklerden aranılan texte ait linki seçer
Find_element_by_tag_name() : Belirli bir etiketi olan Html elementleri seçer
Find_element_by_class_name() : Class’ı olan, elementi name’i ile seçer
Find_element_by_css_selector() : Css selectorunu kullanarak elemente erişimi sağlar 
Find_element_by_partial_link_text() : belirli bir metin içeriğini kullanır 
Quit () : tarayıcı kapatmak için kullanılır

"""