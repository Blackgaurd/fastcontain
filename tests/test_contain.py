from fastcontain import FastContain

with open("tests/lorem.txt", "r") as f:
    lorem = FastContain(f.read())


def test_small_string():
    # contains
    assert "en pelle" in lorem
    assert "uam e" in lorem
    assert "ollicitudin " in lorem
    assert "corper a l" in lorem
    assert "onvallis a. Phasel" in lorem

    # not contains
    assert "sts Facil" not in lorem
    assert "enatfbus et maasi" not in lorem
    assert "simdia " not in lorem
    assert "proen nibh nisl condimentum. Mi" not in lorem
    assert "ghbjcp2 asd" not in lorem


def test_medium_string():
    assert (
        "lisis volutpat est velit egestas dui id. Pulvinar etiam non quam lacus. Sit amet consectetur adipiscing elit pellentesque. Vel facilisis volutpat est velit egestas. Non quam lacus suspendisse faucibus interdum posuere lorem ipsum. Penatibus et magnis dis parturient. Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla. Risus ultricies tristique nulla aliquet enim tortor at auctor urna. Sapien pellentesque habitant morbi tristique senectus et netus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum varius. Amet mattis vulputate enim nulla. Sed vulputate mi sit amet mauris. Ornare arcu dui vivamus arcu felis bibendum ut. Tempor orci dapibus ultrices in iaculis. At ultrices mi tempus imperdiet nulla malesuada pellentesque elit. Mi in nulla posuere sollicitudin aliquam ultrices.\nA condi"
        in lorem
    )
    assert (
        "tus aliquam eleifend mi in. Consectetur adipiscing elit ut aliquam purus sit. Laoreet sit amet cursus sit amet dictum sit amet justo. Sodales ut etiam sit amet nisl purus in mollis nunc. Enim nunc faucibus a pellentesque sit amet. Diam ut venenatis tellus in metus vulputate eu. Enim eu turpis egestas pretium aenean. Ac odio tempor orci dapibus ultrices in iaculis nunc sed. Nullam non nisi est sit amet facilisis. Nisl condimentum id venenatis a condimentum vitae. In ante metus dictum at tempor commodo. Nisi est sit amet facilisis magna etiam tempor orci eu. Sit amet porttitor eget dolor morbi non arcu. Adipiscing bibendum est ultricies integer quis auctor elit. Cras tincidunt lobortis feugiat vivamus at augue.\nAmet nisl purus in mollis. Faucibus pu"
        in lorem
    )
    assert (
        "sis volutpat est velit egestas dui id. Pulvinar etiam non quam lacus. Sit amet consectetur adipiscing elit pellentesque. Vel facilisis volutpat est velit egestas. Non quam lacus suspendisse faucibus interdum posuere lorem ipsum. Penatibus et magnis dis parturient. Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla. Risus ultricies tristique nulla aliquet enim tortor at auctor urna. Sapien pellentesque habitant morbi tristique senectus et netus. Et ligula ullamcorper malesuada proin libero nunc consequat interdum varius. Amet mattis vulputate enim nulla. Sed vulputate mi sit amet mauris. Ornare arcu dui vivamus arcu felis bibendum ut. Tempor orci dapibus ultrices in iaculis. At ultrices mi tempus imperdiet nulla malesuada pellentesque elit. Mi in nulla posuere sollicitudin aliquam ultri"
        in lorem
    )
