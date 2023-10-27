def my_name_is():
    print("My name is Asmaul Husna")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"

item_list = [
    {
        
        "course" : "python & web",
        "backend" : "python",
        "frontend" : "html, css, bootstrap"
    },
     {
        
        "course" : "java spring boot",
        "backend" : "java",
        "frontend" : "html, css, hibernet"
    },
     {
        
        "course" : "c# & ASP.NET Core",
        "backend" : "C#, Entity Framework",
        "frontend" : "Razor"
    },
     {
        
        "course" : "MERN Development",
        "backend" : " Node, React",
        "frontend" : "html, css,"
    },
     {
        
        "course" : "PHP & Laravel",
        "backend" : "PHP",
        "frontend" : "Blade, Eloquent"
    },
   
]



for item in item_list:
    course_name = item["course"]
    backend = item["backend"]
    frontend = item["frontend"]




    my_name_is()
    i_have_enrolled_course("Python & Web")
    result = i_have_learning("Python", "HTML, CSS, JavaScript")
    print(result)


    my_name_is()
    i_have_enrolled_course("java spring boot")
    result = i_have_learning("java", "html, css, hibernet")
    print(result)

    my_name_is()
    i_have_enrolled_course("c# & ASP.NET Core")
    result = i_have_learning("c#,Entity Framework", "Razor")
    print(result)

    my_name_is()
    i_have_enrolled_course("MERN Development")
    result = i_have_learning("Node, React", "html, css")
    print(result)

    my_name_is()
    i_have_enrolled_course("PHP & Laravel")
    result = i_have_learning("PHP", "Blade, Eloquent")
    print(result)

