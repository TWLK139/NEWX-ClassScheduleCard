<template>
	<view id="about">
		<view id="aboutContentBox">
			<view id="conPic">
				<image src="http://img.wh241.cn/img/20190907/Ee4kSAgSfFBI.png?imageslim"></image>
				<view id="conPicWord">查课系统 · 2020</view>
				<view style="font-size: 70%;color: #a8a8a8;">NEWX创作</view>
			</view>
			<view class="conView">
				<view class="conTitle">关于查课系统</view>
				<view class="conWord">{{ about.system }}</view>
				<!-- <view class="conLink"></view> -->
			</view>
			<view class="conView">
				<view class="conTitle">关于我们</view>
				<view class="conWord">{{ about.us }}</view>
				<view class="conLink">
					<view @click="handleUrl('http://mobile.newxstudio.com', false, '合肥工业大学宣城校区大学生网络文化工作室官方网站网址')">了解NEWX</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue'

	export default {
		data() {
			return {
				about: {
					system: '目前功能：按条件查询课程情况可实现更加便捷地选课、调课和旁听，同时可以查找自习教室、获取课程信息、快速比对多个课程。课表展示功能可以展示学生本人课程信息、自行添加教务课表无法查询的课程信息并可以实现断网查看课表。成绩计算功能可以方便学生查询和计算绩点。考试信息查询可以为学生提供便捷的近期考试信息查询、允许学生自行添加考试信息并可以实现断网查看考试信息。同时，本软件可随时清理本地记录，不保留任何学生信息，有效保护用户隐私。',
					us: 'NEWX为合肥工业大学宣城校区的同学设计了该课程平台，NEWX可以完成网页设计、媒体平台管理、视频制作、摄影摄像、图文编辑等工作，旨在宣传优秀的校园文化，提高同学对多媒体技术的兴趣。'
				}
			}
		},
		onLoad() {
			uni.request({
				url: Vue.config.baseUrl[0] + 'getabout',
				method: 'GET',
				success: (res) => {
					if (res.data.code == this.code.success) {
						this.about = res.data.data;
					} else {
						this.error.server();
					}
				},
				fail: (res) => {
					this.error.internet();
				}
			})
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {}
	}
</script>

<style>
	@import url('./about.css');
</style>
