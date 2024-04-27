from playwright.sync_api import sync_playwright

import pandas as pd





def maina(search_for, total):
    l1=[]
    l2=[]

    Name = ""
    Address = ""
    Website = ""
    Phone_Number = ""
    Reviews_Count = 0
    Reviews_Average = 0
   

    names_list=[]
    address_list=[]
    website_list=[]
    phones_list=[]
    reviews_c_list=[]
    reviews_a_list=[]
    
       
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/maps/@32.9817464,70.1930781,3.67z?", timeout=60000)
        page.wait_for_timeout(5000)

        page.locator('//input[@id="searchboxinput"]').fill(search_for)
        page.wait_for_timeout(5000)

        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)

       
        page.hover('//a[contains(@href, "https://www.google.com/maps/place")]')

        
        previously_counted = 0
        while True:
            page.mouse.wheel(0, 10000)
            page.wait_for_timeout(3000)

            if (page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]').count() >= total):
                listings = page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]').all()[:total]
                listings = [listing.locator("xpath=..") for listing in listings]
                print(f"Total Found: {len(listings)}")
                break
            else: #The loop should not run infinitely
                if (page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]' ).count() == previously_counted ):
                    listings = page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]' ).all()
                    print(f"Arrived at all available\nTotal Found: {len(listings)}")
                    break
                else:
                    previously_counted = page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]' ).count()
                    print( f"Currently Found: ", page.locator( '//a[contains(@href, "https://www.google.com/maps/place")]' ).count(), )


        for listing in listings:
            listing.click()
            page.wait_for_timeout(3000)
           
            name_xpath = '//div[@class="TIHn2 "]//h1[@class="DUwDvf lfPIob"]'
            address_xpath = '//button[@data-item-id="address"]//div[contains(@class, "fontBodyMedium")]'
            website_xpath = '//a[@data-item-id="authority"]//div[contains(@class, "fontBodyMedium")]'
            phone_number_xpath = '//button[contains(@data-item-id, "phone:tel:")]//div[contains(@class, "fontBodyMedium")]'
            reviews_count_xpath = '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span//span//span[@aria-label]'
            reviews_average_xpath = '//div[@class="TIHn2 "]//div[@class="fontBodyMedium dmRWX"]//div//span[@aria-hidden]'
            
            
          
            
           
            
            if page.locator(reviews_count_xpath).count() > 0:
                temp = page.locator(reviews_count_xpath).inner_text()
                temp=temp.replace('(','').replace(')','').replace(',','')
                Reviews_Count=float(temp)
                reviews_c_list.append(Reviews_Count)
                print(reviews_c_list)
            else:
                Reviews_Count = ""
                reviews_c_list.append(Reviews_Count)

            if page.locator(reviews_average_xpath).count() > 0:
                temp = page.locator(reviews_average_xpath).inner_text()
                temp = temp.replace(' ','').replace(',', '.')
                Reviews_Average=float(temp)
                reviews_a_list.append(Reviews_Average)
                print(reviews_a_list)
            else:
                Reviews_Average = ""
                reviews_a_list.append(Reviews_Average)
            if page.locator(name_xpath).count() > 0:
                Name = page.locator(name_xpath).inner_text()
                names_list.append(Name)
                print(names_list)
                #l1.append(page.locator(name_xpath).inner_text())
            else:
                Name = ""
                names_list.append(Name)
            if page.locator(address_xpath).count() > 0:
                Address = page.locator(address_xpath).inner_text()
                address_list.append(Address)
                print(address_list)
            else:
                Address = ""
                address_list.append(Address)
            if page.locator(website_xpath).count() > 0:
                Website = page.locator(website_xpath).inner_text()
                website_list.append(Website)
                print(website_list)
            else:
                Website = ""
                website_list.append(Website)
            if page.locator(phone_number_xpath).count() > 0:
                Phone_Number = page.locator(phone_number_xpath).inner_text()
                phones_list.append(Phone_Number)
                print(phones_list)
            else:
                Phone_Number = ""
                phones_list.append(Phone_Number)
           
   
            
            
        
        
        df = pd.DataFrame(list(zip(names_list, website_list,phones_list,address_list,reviews_c_list,reviews_a_list)), columns =['Names','Website','Phone_Number','Address','Review_Count','Average_Review_Count'])
        for column in df.columns:
            if df[column].nunique() == 1:
                df.drop(column, axis=1, inplace=True)
        df.to_csv(r'efwewfws.csv', index = False)
        return df
        browser.close()
        
        l1=[]
        l2=[]

        Name = ""
        Address = ""
        Website = ""
        Phone_Number = ""
        Reviews_Count = 0
        Reviews_Average = 0
        Store_Shopping = ""
        In_Store_Pickup = ""
        Store_Delivery = ""
        Place_Type = ""
        Opens_At = ""
        Introduction = ""

        names_list=[]
        address_list=[]
        website_list=[]
        phones_list=[]
        reviews_c_list=[]
        reviews_a_list=[]
        store_s_list=[]
        in_store_list=[]
        store_del_list=[]
        place_t_list=[]
        open_list=[]
        intro_list=[]
        



if __name__ == "__main__":
  
        tipo_de_negocio = "Electronica"
        pais = "Argentina"
        estado_ciudad = ""
        search_for = tipo_de_negocio + " en  "+estado_ciudad +" "+pais 
   
        total = 6

        maina(search_for, total)
