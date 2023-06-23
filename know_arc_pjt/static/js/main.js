// 페이지 버튼
$(document).ready(function($) {

    $(".scroll_move").click(function(event){         

            event.preventDefault();

            // $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);

    });

});


// 검색
function searchKeyword(){
    let searchValue = document.getElementById('search-input').value.trim();
    if (searchValue.length > 1){
        location.href="/search/" + searchValue + "/";
    }
    else{
        alert('검색어('+ searchValue +')가 너무 짧습니다.');
    }
};

document.getElementById('search-input').addEventListener('keyup', function(event){
    if(event.key === 'Enter'){
        searchKeyword();
    }
});