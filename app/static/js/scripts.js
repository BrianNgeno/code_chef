$('document').ready(()=>{
  $('#createform').submit((event)=>{
    event.preventDefault()
    pitch=$('#pitch_ideas').val().trim()
    category=$('#catchoose').val().trim()
    if (pitch.length < 2){return}
    $.ajax(
      {
        url:'/newproject',
        data:{
          'pitch_ideas':pitch,
          'category':category
        },
        method:'GET',
        success:(data)=>{
          $("#pitches").prepend(data)
          $('#createform')[0].reset()
        },
        error: (data)=>{
          alert('Could not post pitch')
        }
      }
    )
  })
  filterelements=c=>{
    $(".post").each((n,elem)=>{elem=$(elem);if(!elem.hasClass(c)){elem.hide('fast')}else{elem.show(50)}})
  }
  complete=(pitch)=>{
    $.ajax(
      {

        url:'/complete/'+pitch
        })
    }
delete_post=(project)=>{
  $('#post'+project).hide(300,()=>{$('#post'+project).remove()});

  $.ajax(
    {

      url:'/delete/'+project
      })
  }
submitcomment=(postid)=>{
$.post('/newcomment/'+postid, $('form#comment'+postid).serialize(),(data)=>{
  $(data).hide().appendTo($('#comments'+postid)).show('fast');
  count=$('#commentscount'+postid)
  count.content(parseInt(count.content())+1)
});
[...$(".commentinput")].forEach(c=>c.value='')
}

});