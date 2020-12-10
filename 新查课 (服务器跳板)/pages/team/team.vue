<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="departChoose">
			<view class="departs" @click="showArtType(0, 0)">文章</view>
			<view class="departs" @click="showArtType(1, 7)">视频</view>
			<view class="departs" @click="showArtType(2, 3)">图文</view>
			<view class="departs" @click="showArtType(3, 8)">采编</view>
			<view class="departs" @click="showArtType(4, 6)">采风</view>
			<view class="departs" @click="showArtType(5, 2)">网站</view>
			<view class="departs" @click="showArtType(6, 9)">办公</view>
			<view id="departActiveLine" :style="{'left': artType*14.28+'%'}"></view>
		</view>
		<navigator class="art_box animated bounceInUp" v-for="(art, i) in showArray" :key="i" :url="'../teamDetail/teamDetail?id='+art.id+'&type='+artType">
			<view class="art_body">
				<image mode="aspectFill" class="art_img" :src="art.img"></image>
				<view class="art_body_describe">
					<view class="art_body_title ellipsis_div">{{ art.title }}</view>
					<view class="art_body_con">{{ art.desca }}</view>
					<view class="art_foot">
						<view class="art_foot_con">{{ art.update_time.substr(5, 11) }}</view>
						<view class="art_foot_con ellipsis_div" style="text-align: right;">{{ artType!=0?"作者：" + art.author:"查看详情" }}</view>
					</view>
				</view>
			</view>
		</navigator>
		<view id="bottom_mes">没有更多数据了……</view>
	</view>
</template>

<script>
	import Vue from 'vue'
	export default {
		data() {
			return {
				showArray: [],
				artType: -1
			}
		},
		onLoad() {
			this.showArtType(0, 0);
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			getNews() {
				uni.request({
					url: Vue.config.baseUrl[4] + 'returnnews',
					method: 'GET',
					success: (res) => {
						if (res.data.code == this.code.success) {
							this.showArray = res.data.data;
						} else {
							this.error.server();
						}
					},
					fail: (res) => {
						this.error.internet();
					},
					complete: (res) => {
						uni.hideLoading();
					}
				});
			},
			showArtType(type, id) {
				if (this.artType != type) {
					this.showArray = [];
					this.artType = type;

					uni.showLoading({
						title: '加载中……'
					});
					if (type == 0) {
						this.getNews();
					} else {
						uni.request({
							url: Vue.config.baseUrl[5] + "returnWorks?department=" + id,
							method: 'GET',
							success: (res) => {
								if (res.data.code == this.code.success) {
									this.showArray = res.data.data;
								} else {
									this.error.server();
								}
							},
							fail: (res) => {
								this.error.internet();
							},
							complete: (res) => {
								uni.hideLoading();
							}
						})
					}
				}
			}
		}
	}
</script>

<style>
	@import url('./team.css');
	@import url("../overall/animate.css");
</style>
