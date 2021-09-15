  function getDog(){
            $.getJSON("https://dog.ceo/api/breeds/image/random", function( data ) {
                $(".json pre").html(JSON.stringify(data, null, 4));
                $(".image-content").html("<img src='" + data.message + "'>");
            });
        }
        $('.get-dog').click(function(){
            getDog();
        });

        $(document).ready(function() {
            getDog();
        });      

