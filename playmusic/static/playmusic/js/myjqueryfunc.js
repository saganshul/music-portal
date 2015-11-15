var test;
$('.queuejquery').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/playmusic/playlistmaker/",
		  data: {
			song_id: catid
		  },
		  success: function( data ) {
			$('#backplaylist').html(data);
            $('#queue'+catid).hide();
		  }
		})
});
$('.playlisttab').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/add/playlist/",
		  data: {
			playlist_song_id: catid
		  },
		  success: function( data ) {
        $('#addtoplaylist'+catid).hide();
		  }
		})
});
$('.favtab').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/add/fav/",
		  data: {
			fav_song_id: catid
		  },
		  success: function( data ) {
        $('#addtofav'+catid).hide();
		  }
		})
});
$('.searchimage').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/playmusic/playit/",
		  data: {
			song_id: catid
		  },
		  success: function( data ) {
			$('#backplaylist').html(data);
            $('#play'+catid).hide();
            location.reload(true);
            $('a#playbutton')[0].click();

		  }
		})
});

$('#searchbutton').click(function(){
    var catid;
    songname = $('#suggestion').val();

     $.ajax({
		  type:"GET",
		  url: "/playmusic/search/",
		  data: {
			name: songname
		  },
		  success: function( data ) {
            $('#matterbox').html(data);

		  }
		})
});
$(function() {
  $("#suggestion").autocomplete({
    source: "/playmusic/suggest_category/",
    minLength: 2,
  });
});
$('#searchbuttonbyartist').click(function(){
    var catid;
    songname = $('#suggestion').val();

     $.ajax({
		  type:"GET",
		  url: "/playmusic/searchbyartist/",
		  data: {
			name: songname
		  },
		  success: function( data ) {
            $('#matterbox').html(data);

		  }
		})
});
$('#searchbuttonbyalbum').click(function(){
    var catid;
    songname = $('#suggestion').val();

     $.ajax({
		  type:"GET",
		  url: "/playmusic/searchbyalbum/",
		  data: {
			name: songname
		  },
		  success: function( data ) {
            $('#matterbox').html(data);

		  }
		})
});
$('#searchbuttonbygenre').click(function(){
    var catid;
    songname = $('#suggestion').val();

     $.ajax({
		  type:"GET",
		  url: "/playmusic/searchbygenre/",
		  data: {
			name: songname
		  },
		  success: function( data ) {
            $('#matterbox').html(data);

		  }
		})
});
$('#searchbysong').click(function(){
    var catid;
    songname = $('#suggestion').val();

     $.ajax({
		  type:"GET",
		  url: "/playmusic/search/",
		  data: {
			name: songname
		  },
		  success: function( data ) {
            $('#matterbox').html(data);

		  }
		})
});
$('#usersearchbutton').click(function(){
    var username;
    username = $('#usersearch').val();
     $.ajax({
		  type:"GET",
		  url: "/playmusic/users/",
		  data: {
			     username: username
		  },
		  success: function( data ) {
            $('#userresult').html(data);
		  }
		})
});
$('.recommendtab').click(function(){
    test = $(this).attr("data-catid");
});

$('.userbutton').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/recommend/friend/",
		  data: {
    			to_user_id: catid,
          rec_song_id: test
		  },
		  success: function( data ) {
        $('#addusertorecommendlist'+catid).hide();
		  }
		})
});
$('.recsection').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/playmusic/playlistmaker/",
		  data: {
			     song_id: catid
		  },
		  success: function( data ) {
			$('#backplaylist').html(data);
            $('#addrectoqueue'+catid).hide();
		  }
		})
});
$('.alerts-link').click(function(){

     $.ajax({
		  type:"GET",
		  url: "/recommend/remove/",

		})
});
$('#playlistbutton').click(function(){
     $.ajax({
		  type:"GET",
		  url: "/playmusic/playmyplaylist/",
      success: function( data ) {
			$('#backplaylist').html(data);
		  }
		})
});
$('#favlistbutton').click(function(){
     $.ajax({
		  type:"GET",
		  url: "/playmusic/playmyfav/",
      success: function( data ) {
			$('#backplaylist').html(data);
		  }
		})
});
$('#userplaylistsearchbutton').click(function(){
    var username;
    username = $('#userplaylistsearch').val();
     $.ajax({
		  type:"GET",
		  url: "/playmusic/usersplaylist/",
		  data: {
			     username: username
		  },
		  success: function( data ) {
            $('#userplaylistresult').html(data);
		  }
		})
});
$('.userplaylistbutton').click(function(){
    var catid;
    catid = $(this).attr("data-catid");

     $.ajax({
		  type:"GET",
		  url: "/playmusic/playotherplaylist/",
		  data: {
			    user_id: catid
		  },
		  success: function( data ) {
          $('#usergayab'+catid).hide();
          location.reload(true);
		  }
		})
});
