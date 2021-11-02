def convertStudent(course):
    groupe = course["grupo"]
    teacher = course["docente"]
    student = course["estudiante"]
    del course["grupo"]
    del course["docente"]
    course = {
        "materia": {**course},
        "grupo": groupe,
        "docente": teacher,
        "estudiante":student,
        "previo_uno": 3.5,
        "previo_dos": 4,
        "previo_tres": 5, 
        "examen_final": 3,
    }
    return course

def convertTeacher(course):
    groupe = course["grupo"]
    teacher = course["docente"]
    del course["grupo"]
    del course["docente"]
    course = {
        "materia": {**course},
        "grupo": groupe,
        "docente": teacher,
    }
    return course
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    