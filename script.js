//Download cv
document.getElementById('butn').addEventListener('click', function() {
    // Replace the placeholder URL with your actual Google Drive resume URL
    var resumeUrl = 'https://drive.google.com/uc?export=download&id=1M8ouX1XgJXKT_vdt8wmwHUfDo6ZaUCiH';

    // Open a new window or tab with the Google Drive URL
    window.open(resumeUrl, '_blank');
});



document.getElementById('git-butn').addEventListener('click', function(){

    var github='https://github.com/Mohammadtalha3?tab=repositories'

    window.open(github,'_blank');
});

document.getElementById('link-butn').addEventListener('click', function(){

    var linkdien= 'https://www.linkedin.com/in/mohammad-talha-92b45a220/'

    window.open(linkdien, '_blank')
})



document.addEventListener('click', function(){
    var skills = document.querySelectorAll('#progress-bar');

    function isElementInViewport(element) {
        var rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    function animateSkills() {
        skills.forEach(function (skill) {
            if (isElementInViewport(skill)) {
                skill.style.width = skill.getAttribute('data-width');
            }
        });
    }

    // Initial animation check
    animateSkills();

    // Scroll event listener
    window.addEventListener('scroll', animateSkills);
});

document.getElementsByClassName('whatsapp-butn')[0].addEventListener('click', function(){

    var whatsapp_pro_link= 'https://mohammadtalha3-chat-analyzer-app-bpwmkc.streamlit.app/'

    window.open(whatsapp_pro_link, '_blank')
})


document.getElementsByClassName('student-butn')[0].addEventListener('click', function(){
    var student= 'https://866d-39-41-139-50.ngrokfree.app/predictdata'

    window.open(student, '_blank')
})

const progressBar = document.querySelector('.progress');
const percentage = 80; // Set your desired percentage

progressBar.style.transform = `rotate(${percentage * 3.6}deg)`;












