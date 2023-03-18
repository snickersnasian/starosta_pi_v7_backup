import requests 

res = requests.get('https://script.googleusercontent.com/macros/echo?user_content_key=WaX5QHttXkVZcVZ22Ey2nOHBU2bQLvEeiDAXFooCmgpc6-43ebteeyCGD857A27d2cO5-7WFyWjo6ADv0TSa514_sEntOZc8m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnLFtk-H9yy4ec9a2mxKfUqZ-n36-ehz6_bjQ5sPEFH16dKYmYu95ifP1i9X11kSk9cZV40ZpOkGQ2LKS0oH9NbDjDAqPkTAbJQ&lib=MTo-mMGpfZ8DxeB-gajX_FU8jPqgvzQIJ')

json_res = res.json()

print(json_res)