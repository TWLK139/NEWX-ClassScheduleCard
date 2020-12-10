<template>
	<view style="width: 100%;overflow-x: hidden;">
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="webTitle">
			<view></view>
			{{ type == 0 ? 'NEWS' : text.department }}
			<view></view>
		</view>
		<view id="newsTitle">
			{{ text.title }}
			<view style="font-size: 30upx;font-weight: 300;">{{ text.update_time }}</view>
		</view>
		<view id="textAuthor">{{ '作者：' + (type == 0 ? '小新' : text.author) }}</view>
		<view class="line"></view>
		<image id="img" mode="aspectFit" :src="text.img" />
		<view id="deca">简介：{{ text.desca }}</view>
		<view class="line"></view>
		<!-- #ifdef APP-PLUS || H5 -->
		<view id="gotoWork" v-if="type == 1 || type == 3 || type == 5" @click="handleUrl(text.url, false, '内容')">点击查看作品</view>
		<!-- #endif -->
		<!-- #ifdef MP-QQ || MP-WEIXIN -->
		<view class="copyUrl" v-if="type == 1 || type == 3 || type == 5" @click="handleUrl(text.url, false, '内容')">内容参考{{ text.url }}</view>
		<!-- #endif -->
		
		<view id="teamText" v-html="text.text"></view>
		<view id="botLine"></view>
		<view id="textCopy">转载请联系作者：{{ type == 0 ? '合肥工业大学宣城校区大学生网络文化工作室' : text.author }}</view>
		<view id="backButton" @click="backButton">返回</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				text: {},
				type: -1
			};
		},
		onLoad(opt) {
			this.type = opt.type;
			let thisUrl = Vue.config.baseUrl[5] + 'getWorksById?id=';
			if (opt.type == 0) {
				thisUrl = Vue.config.baseUrl[4] + 'getnewsbyid?id=';
			}
			uni.request({
				url: thisUrl + opt.id,
				method: 'GET',
				success: res => {
					if (res.data.code == this.code.success) {
						// #ifdef H5
						res.data.data.text = res.data.data.text.replace(/width: 600px;/g, "width: 100%");
						// #endif
						this.text = res.data.data;
					} else {
						this.error.server();
					}
				},
				fail: res => {
					this.error.internet();
				}
			});
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			backButton() {
				uni.navigateBack();
			}
		}
	};
</script>

<style>
	@import url('./teamDetail.css');
</style>
