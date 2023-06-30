// 페이지 버튼
$(document).ready(function($) {

    $(".scroll_move").click(function(event){         

            event.preventDefault();

            // $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);

    });

});


document.addEventListener("keyup", function(event) {
    if (event.key === 'Enter') {
        searchKeyword();
    }
});
// 검색
function searchKeyword(){
    let searchValue = document.getElementById('search-input').value.trim();
    if (searchValue.length > 1){
        location.href="/search/" + searchValue + "/" + "#page2";
        
    }
    else{
        alert('검색어('+ searchValue +')가 너무 짧습니다.');
    }
    
    
};


// 검색창 박스, submit 이벤트 감지를 위해 변수 선언
let chatForm = document.querySelector('.searchPart')
// 준비 함수, 약간의 시간을 두어 scroll 함수 호출
function prepareScroll() {
    window.setTimeout(scrollUI, 50);
}
// scroll 함수
function scrollUI() {
    // 검색창 요소
    let chatUI = document.querySelector('.sch_go');
    chatUI.scrollTOP = chatUI.scrollHeight;
}

chatForm.addEventListener('submit', prepareScroll);

// $( document ).ready(function() {
//     var offset = $("#").offset();
//     $('html, body').animate({scrollTop : offset.top}, 400);
//  });

// // document.getElementById('search-input').addEventListener('keydown', function(event){
//     if(event.key === 'Enter'){
//         
//     }
// });


// 동석님 검색



