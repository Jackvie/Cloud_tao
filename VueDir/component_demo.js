$(function(){
    // Define a new component called todo-item
    Vue.component('todo-item', {
      template: '<li>This is a todo</li>'
    });
    
    var vm = new Vue({
        el: '#app',
        data :{}
    });
    
    //////////////////////////////

    Vue.component('todo-item-2', {
		// The todo-item component now accepts a
		// "prop", which is like a custom attribute.
		// This prop is called todo.
		props: ['todo'],
		template: '<li>{{ todo.text }}</li>'
	});

	var vm2 = new Vue({
		el: '#app-2',
		data: {
			groceryList: [
				{ text: 'Vegetables' },
				{ text: 'Cheese' },
				{ text: 'Whatever else humans are supposed to eat' }
			]
		}
	});
})