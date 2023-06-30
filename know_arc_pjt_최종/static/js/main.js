// 페이지 버튼
$(document).ready(function($) {

    $(".scroll_move").click(function(event){         

            event.preventDefault();

            // $('html,body').animate({scrollTop:$(this.hash).offset().top}, 500);

    });

});


<<<<<<< HEAD


// 검색
document.addEventListener("keyup", function(event) {
    if (event.key === 'Enter') {
        searchKeyword();
    }
});

function searchKeyword(){
    let searchValue = document.getElementById('search-input').value.trim();
    if (searchValue.length > 1){
        location.href="/search/" + searchValue + "/#page2";
        
=======
// 검색
function searchKeyword(){
    let searchValue = document.getElementById('search-input').value.trim();
    if (searchValue.length > 1){
        location.href="/search/" + searchValue + "/";
>>>>>>> 63140d75cb74c4abeacb41c98c57d6d40de94777
    }
    else{
        alert('검색어('+ searchValue +')가 너무 짧습니다.');
    }
<<<<<<< HEAD
    
    
};


// 동석님 검색



// 경민님 차트
=======
};

document.getElementById('search-input').addEventListener('keyup', function(event){
    if(event.key === 'Enter'){
        searchKeyword();
    }
});
>>>>>>> 63140d75cb74c4abeacb41c98c57d6d40de94777
