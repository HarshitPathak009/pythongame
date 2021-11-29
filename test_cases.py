#Write the test cases and the test script for automating
cases = [
    {
        "board":[
        [10,0,0,0,0,0,0,0],
        [0,0,20,0,0,0,0,0],
        [0,0,0,0,0,20,40,0],
        [0,0,40,0,10,10,20,0],
        [0,0,0,0,0,0,0,0],
        [0,0,20,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,10,0,0,0,0,0]
        ],
        "output": True
    },

    {
        "board": [
                [0]*8
            ]*8,
        "output": False
    },

    {
        "board": [
                []
            ],
        "output": False
    },

    {
        "board": [
                []
            ],
        "output": True
    },

    {
        "board": [
                []
            ],
        "output": False
    },
]