function Predict() 
{
    const ageId = document.getElementById("age");
    age = ageId.value

    const genderId = document.getElementById("gender");
    gender = genderId.value

    const departmentId = document.getElementById("department");
    department = departmentId.value

    const titleId = document.getElementById("title");
    title = titleId.value

    const experienceId = document.getElementById("experience");
    experience = experienceId.value

    const educationId = document.getElementById("education");
    education = educationId.value

    const locationId = document.getElementById("location");
    location = locationId.value



    values = [age,gender,department,title,experience,education,location];

    if (values.some(element => element === "")) {
        window.location.href = "/";
        return;
    }


    window.location.href = `/predict/load?age=${encodeURIComponent(age)}&gender=${encodeURIComponent(gender)}&department=${encodeURIComponent(department)}&title=${encodeURIComponent(title)}&experience=${encodeURIComponent(experience)}&education=${encodeURIComponent(education)}&location=${encodeURIComponent(location)}`
}

function Back()
{
    window.location.href = "/";
}