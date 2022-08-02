import requests
import lxml.html as lh


def gender_genie(text, genre):
    url = 'http://bookblog.net/gender/analysis.php'
    caption = 'The Gender Genie thinks the author of this passage is:'

    form_data = {
        'text': text,
        'genre': genre,
        'submit': 'submit',
    }

    response = requests.post(url, data=form_data)

    tree = lh.document_fromstring(response.content)

    return tree.xpath("//b[text()=$caption]", caption=caption)[0].tail.strip()


if __name__ == '__main__':
    print(gender_genie('I have a beard!', 'blog'))