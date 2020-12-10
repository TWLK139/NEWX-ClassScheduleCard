<script>
	import Vue from 'vue';
	export default {
		onLaunch: function() {
			uni.getSystemInfo({
				success: function(e) {
					// #ifndef MP
					Vue.prototype.StatusBar = e.statusBarHeight;
					if (e.platform == 'android') {
						Vue.prototype.CustomBar = e.statusBarHeight + 50;
					} else {
						Vue.prototype.CustomBar = e.statusBarHeight + 45;
					}
					// #endif
				}
			});
		},
		onShow() {
			this.simpleCheck();
		}
	};
</script>

<style>
	uni-picker .uni-picker-item {
		font-size: 14px !important;
	}
</style>
