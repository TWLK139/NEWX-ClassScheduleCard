var feedBackBox = new Vue({
    	el: '#feedBackBox',
    	data: {
    		list: [],
    	},
    	mounted() {
    		this.$http.get('http://www.newxstudio.com/index/feedback/flist').then(res => {
    			this.list = res.data.data.splice(29);
    		})
    	}
    })
