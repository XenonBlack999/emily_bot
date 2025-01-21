# -*- coding: utf-8 -*-
"""
in this module have to check internet and 
another functions which related with internet

@author: Administrator
"""
try:
    import speedtest
except:
    print("error")

def test_speedtest_setup():
        try:
            st = speedtest.Speedtest()
            best_server = st.get_best_server()
            print(f"Connected to {best_server['host']} located in {best_server['country']}.")

            return True
        except Exception as e:
            print(f"Error during speedtest setup: {e}")
            return False
        
        
        
def check_internet_speed():
        st = speedtest.Speedtest()

        st.get_best_server()


        download_speed = st.download() / 1_000_000  
        upload_speed = st.upload() / 1_000_000      


        return {
            'download_speed_mbps': round(download_speed, 2),
            'upload_speed_mbps': round(upload_speed, 2)
        }
    