from zipfile import ZipFile

def test_zip():
    with ZipFile("Resources/Archiv.zip") as zip_:
        print(zip_.namelist())
        text = zip_.read("text")
        print(text)
        zip_.extract("text")
        zip_.extract("text", "C:\Users\sviat\PycharmProjects\pythonProject\Resources")

    assert zip_.read() and zip_.open() in text