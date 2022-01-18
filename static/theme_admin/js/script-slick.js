
 

//SLICK 


(function(jQuery){
    var tabCarousel = jQuery('.addproduct-js');
        if (tabCarousel.length) {
            
            tabCarousel.each(function(){
                var thisCarousel = jQuery(this),
                    item =  jQuery(this).data('item'),
                    itemmobile =  jQuery(this).data('itemmobile');
                    
                        
                
                thisCarousel.slick({
                    
                    dots: false,
                    arrows: true,
                    infinite: true,
                    //rtl:true,
                    speed: 300,
                    slidesToShow: item || 4,
                    slidesToScroll: item || 4,
                    adaptiveHeight: true,
                    autoplay: false,
                        responsive: [{
                            breakpoint: 1025,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll:3
                            }
                        },
                        {
                            breakpoint: 791,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2
                            }
                        },
                    {
                        breakpoint: 650,
                        settings: {
                            slidesToShow: itemmobile || 1,
                            slidesToScroll: itemmobile || 1,
                        }
                    }]
                });
            });
        };
        
  })(jQuery);  
(function(jQuery){
  var tabCarousel = jQuery('.slick-multiple-arrow-js');
      if (tabCarousel.length) {
          
          tabCarousel.each(function(){
              var thisCarousel = jQuery(this),
                  item =  jQuery(this).data('item'),
                  itemmobile =  jQuery(this).data('itemmobile');
                  
                      
              
              thisCarousel.slick({
                  dots: false,
                  arrows: true,
                  infinite: true,
                  //rtl:true,
                  speed: 300,
                  slidesToShow: item || 2,
                  slidesToScroll: item || 2,
                  adaptiveHeight: true,
                  autoplay: true,
                  autoplaySpeed: 2000,
                      responsive: [{
                          breakpoint: 1025,
                          settings: {
                              slidesToShow: 3,
                              slidesToScroll:3
                          }
                      },
                      {
                          breakpoint: 791,
                          settings: {
                              slidesToShow: 2,
                              slidesToScroll: 2
                          }
                      },
                  {
                      breakpoint: 650,
                      settings: {
                          slidesToShow: itemmobile || 1,
                          slidesToScroll: itemmobile || 1,
                      }
                  }]
              });
          });
      };
      
})(jQuery);  

(function(jQuery){
  var tabCarousel = jQuery('.slick-multiple-Dots-js');
      if (tabCarousel.length) {
          
          tabCarousel.each(function(){
              var thisCarousel = jQuery(this),
                  item =  jQuery(this).data('item'),
                  itemmobile =  jQuery(this).data('itemmobile');
                  
                      
              
              thisCarousel.slick({
                  dots: true,
                  arrows: false,
                  infinite: true,
                  //rtl:true,
                  speed: 300,
                  slidesToShow: item || 2,
                  slidesToScroll: item || 2,
                  adaptiveHeight: true,
                  autoplay: true,
                  autoplaySpeed: 2000,
                      responsive: [{
                          breakpoint: 1025,
                          settings: {
                              slidesToShow: 3,
                              slidesToScroll:3
                          }
                      },
                      {
                          breakpoint: 791,
                          settings: {
                              slidesToShow: 2,
                              slidesToScroll: 2
                          }
                      },
                  {
                      breakpoint: 650,
                      settings: {
                          slidesToShow: itemmobile || 1,
                          slidesToScroll: itemmobile || 1,
                      }
                  }]
              });
          });
      };
      
})(jQuery);  
jQuery('.slick-basic-arrow-js').slick({
  dots: false,
  arrows: true,
  infinite: true,
  speed: 300,
  slidesToShow: 1
});
jQuery('.slick-basic-dot-js').slick({
  dots: true,
  arrows: false,
  infinite: true,
  speed: 300,
  slidesToShow: 1
});
 

(function(jQuery){
    var tabCarousel = jQuery('.productCard-js');
        if (tabCarousel.length) {
            
            tabCarousel.each(function(){
                var thisCarousel = jQuery(this),
                    item =  jQuery(this).data('item'),
                    itemmobile =  jQuery(this).data('itemmobile');
                    
                        
                
                thisCarousel.slick({
                    dots: true,
                    arrows: false,
                    infinite: true,
                    //rtl:true,
                    speed: 300,
                    slidesToShow: item || 4,
                    slidesToScroll: item || 4,
                    adaptiveHeight: true,
                    autoplay: true,
                    autoplaySpeed: 2000,
                        responsive: [{
                            breakpoint: 1300,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll:3
                            }
                        },
                        {
                            breakpoint: 1150,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2
                            }
                        },
                        {
                            breakpoint: 992,
                            settings: {
                                slidesToShow: 3,
                                slidesToScroll: 3
                            }
                        },
                        {
                            breakpoint: 768,
                            settings: {
                                slidesToShow: 2,
                                slidesToScroll: 2
                            }
                        },
                    {
                        breakpoint: 650,
                        settings: {
                            slidesToShow: itemmobile || 1,
                            slidesToScroll: itemmobile || 1,
                        }
                    }]
                });
            });
        };
        
  })(jQuery);  

  
// (function(jQuery){
//     var tabCarousel = jQuery('.mediacat-js');
//         if (tabCarousel.length) {
            
//             tabCarousel.each(function(){
//                 var thisCarousel = jQuery(this),
//                     item =  jQuery(this).data('item'),
//                     itemmobile =  jQuery(this).data('itemmobile');
                    
                        
                
//                 thisCarousel.slick({
//                     dots: true,
//                     arrows: false,
//                     infinite: true,
//                     //rtl:true,
//                     speed: 300,
//                     slidesToShow: item || 8,
//                     slidesToScroll: item || 1,
//                     adaptiveHeight: true,
//                     autoplay: true,
//                     autoplaySpeed: 2000,
//                         responsive: [{
//                             breakpoint: 1300,
//                             settings: {
//                                 slidesToShow: 3,
//                                 slidesToScroll:3
//                             }
//                         },
//                         {
//                             breakpoint: 1150,
//                             settings: {
//                                 slidesToShow: 2,
//                                 slidesToScroll: 2
//                             }
//                         },
//                         {
//                             breakpoint: 992,
//                             settings: {
//                                 slidesToShow: 3,
//                                 slidesToScroll: 3
//                             }
//                         },
//                         {
//                             breakpoint: 768,
//                             settings: {
//                                 slidesToShow: 2,
//                                 slidesToScroll: 2
//                             }
//                         },
//                     {
//                         breakpoint: 650,
//                         settings: {
//                             slidesToShow: itemmobile || 1,
//                             slidesToScroll: itemmobile || 1,
//                         }
//                     }]
//                 });
//             });
//         };
        
//   })(jQuery);  

  jQuery(document).ready(function() {
    var $slider = jQuery('.mediacat-js');
    var $progressBar = jQuery('.progress');
    var $progressBarLabel = jQuery( '.slider__label' );
    
    $slider.on('beforeChange', function(event, slick, currentSlide, nextSlide) {   
      var calc = ( (nextSlide) / (slick.slideCount-1) ) * 100;
      
      $progressBar
        .css('background-size', calc + '% 100%')
        .attr('aria-valuenow', calc );
      
      $progressBarLabel.text( calc + '% completed' );
    });
    
    $slider.slick({
      slidesToShow: 10,
      slidesToScroll: 1,
      dots: false,
      arrows: false,
      speed: 400
    });  
  });