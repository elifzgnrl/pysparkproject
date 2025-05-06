# pysparkproject

Bu repo, Databricks üzerinde gerçekleştirilen bir satış analizi projesini içermektedir.

## 📂 İçerik

- **`pyspark_sales_analysis.ipynb`**: Satış verileri analizi için hazırlanan notebook.  
  👉 [Notebook'u buradan görüntüleyin](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/1994417465611431/2051195365442482/6359647135492093/latest.html)
  
- **`sales_csv.txt`**: Satış verileri dosyası.
- **`menu_csv.txt`**: Menü bilgileri dosyası.

## 🚀 Nasıl Çalıştırılır?

1. **Veri Dosyalarını Yükleme:**  
   `sales_csv.txt` ve `menu_csv.txt` dosyalarını Databricks’te `/FileStore/tables/` dizinine yükleyin.  
   🔹 **Nasıl Yüklenir?**  
   - Databricks sol menüsünden **Data → Add Data → Upload File** adımlarını izleyin.
   - Dosyalar yüklendikten sonra otomatik olarak `/FileStore/tables/` dizininde görünecektir.

2. **Notebook'u Çalıştırma:**  
   - `pyspark_sales_analysis.ipynb` dosyasını Databricks'te açın.
   - Tüm hücreleri sırasıyla çalıştırın.

## 📊 Dashboard

Oluşturulan dashboard'u aşağıdaki bağlantı üzerinden inceleyebilirsiniz:  
👇  
[Dashboard'u görüntüle](https://community.cloud.databricks.com/editor/notebooks/2051195365442482/dashboards/ac9a80dc-ca04-4e10-83d7-5bbbdab534c7)

---

## 🛠 Kullanılan Teknolojiler

- **PySpark**
- **Databricks**
- **GitHub**

## ✍️ Notlar

- Databricks’e veri yüklerken dosya yollarına dikkat edin: `/FileStore/tables/` yolunu doğru şekilde kullanmanız gerekir.
- Eğer Databricks ile GitHub arasında doğrudan bağlantı kurmak isterseniz, Databricks’in **Repos** özelliğini kullanarak GitHub repo'nuzu bağlayabilirsiniz.

