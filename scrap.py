import requests
from bs4 import BeautifulSoup
import os
def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
            print('Writing: ', name)

imagedown('https://www.google.com/search?q=bronz+household+items&tbm=isch&ved=2ahUKEwjvgdSz6-L5AhXlhNgFHd-RDu0Q2-cCegQIABAA&oq=bronz+household+items&gs_lcp=CgNpbWcQAzoECAAQQzoFCAAQgAQ6BAgjECc6CwgAEIAEELEDEIMBOggIABCABBCxAzoECAAQAzoHCCMQ6gIQJzoHCAAQsQMQQzoECAAQHjoGCAAQHhAIOgYIABAKEBhQ0AlY0Elg8UpoAXAAeASAAa0CiAGSJpIBCDAuMTkuNy4xmAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=o9wHY6-kO-WJ4t4P36O66A4&bih=656&biw=1519&rlz=1C1CHBF_enIN885IN885&hl=en#imgrc=QtjTpSDBz_t_RM','bonze')
