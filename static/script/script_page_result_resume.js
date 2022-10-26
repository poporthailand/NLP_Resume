$(document).ready(function () {
    data_length = $("#data_length").text()
    text_skills = $("#text_skills").text().split(",")
    console.log(text_skills);
    // for (let index = 0; index < data_length; index++) {
    //     template_skills = ""
    //     id_skills = '#skills_' + index
    //     data_skills = $(id_skills).text().replace(/[\[\]']/g , "").split(",")

    //     for (let index_text = 0; index_text < text_skills.length; index_text++) {

    //         for (let index_data = 0; index_data < data_skills.length; index_data++) {
    //             if (data_skills[index_data].trim() == text_skills[index_text].trim()){
    //                 template_skills += ',\'' + "Done" + '\''
    //             }
    //             else{
    //                 if (template_skills.length == 0){
    //                     template_skills += '\'' + data_skills[index_data].trim() + '\''
    //                 }
    //                 else {
    //                     template_skills += ',\'' + data_skills[index_data].trim() + '\''
    //                 }
                    
    //             }
                
    //         }

    //     }
    //     $(id_skills).html('<span class="d-flex flex-wrap">'+ template_skills +'</span>')
    // }
    

});