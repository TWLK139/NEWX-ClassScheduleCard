<template>
	<web-view :webview-styles="webviewStyles" :src="src"></web-view>
</template>

<script>
	export default {
		data() {
			return {
				src: '',
				webviewStyles: {
					progress: {
						coler: '#007aff'
					}
				}
			};
		},
		onLoad: function(option) {
			this.src = option.src;
			// #ifndef H5
			if (option.copy == '1')
				uni.setClipboardData({
					data: this.src,
					success: () => {
						uni.showModal({
							title: '温馨提示',
							content: '此网站是学校官方网站，使用电脑浏览器登录体验更佳哦，网址已经复制到剪贴板，快去粘帖吧！',
							showCancel: false,
							confirmText: '我知道了'
						});
					}
				});
			// #endif
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		}
	};
</script>

<style></style>
