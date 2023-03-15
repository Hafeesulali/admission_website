odoo.define('admission_website.college_admission',function(require){
var PublicWidget = require('web.public.widget');
   PublicWidget.registry.PublicWidgetAdmission=PublicWidget.Widget.extend({
   selector:'.admission',
   events:{
        'click #same_as_communication':'click_function'
   },
   click_function:function(ev){
   var checkbox=this.$("#same_as_communication");
   console.log(checkbox);
   if (checkbox.is(':checked')){
   $("#permanent_address_label").hide()
   $('#permanent_address').hide()}
   else{
   $("#permanent_address_label").show()
   $('#permanent_address').show()}
   }
   });





});