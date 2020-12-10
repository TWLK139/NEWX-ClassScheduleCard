<template>
	<view>
		<image id="bgimg" src="../../static/my/bag.png"></image>
		<view id="feedBackBox">
			<input class="con" maxlength="20" v-model="submitText.titile" placeholder="标题"/>
			<input class="con" style="width: 44.8%;padding: 5% 0 5% 5%;" maxlength="10" v-model="submitText.type" placeholder="类型"/>
			<input class="con" style="width: 44.8%;padding: 5% 0 5% 5%;" type="number" maxlength="20" v-model="submitText.qq" placeholder="QQ号"/>
			<textarea class="con" maxlength="400" v-model="submitText.con" style="height: 500upx;" placeholder="内容"></textarea>
<!-- 			<view id="gotoAsk">
				<view class="gotoAskCon">为解决？</view>
				<view class="gotoAskCon" style="text-align: right;">联系技术人员 > </view>
			</view> -->
			<view id="submitButton" @click="feedBack">提交</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue';
	export default {
		data() {
			return {
				submitText: {
					titile: '',
					type: '',
					con: '',
					qq: ''
				},
				student_id:''
			}
		},
		onLoad() {
			this.simpleCheck((res)=>{
				this.student_id = res;
			});
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			feedBack() {
				if (this.submitText.con == '') {
					uni.showToast({
						title: '请输入内容！',
						icon: 'none'
					});
				} else {
					uni.showLoading({
						title: '正在提交……',
						mask:true
					});
					uni.request({
						url: Vue.config.baseUrl[3] + 'feedback?title=' + this.submitText.titile + '&type=' + this.submitText.type +
							'&content=' + this.submitText.con + '&username=' + this.student_id + '&qq=' + this.submitText.qq,
						method: 'GET',
						header: {
							'content-type': 'application/x-www-form-urlencoded',
						},
						success: (res) => {
							uni.hideLoading();
							if (res.data.code == this.code.success) {
								uni.showModal({
									title: '成功',
									content: '提交成功，请关注用户手册。',
									showCancel: false,
									confirmText: '确认',
									success: (res) => {
										this.submitText.titile = '';
										this.submitText.type = '';
										this.submitText.con = '';
										this.submitText.qq = '';
									}
								});
							} else {
								uni.showModal({
									title: '失败',
									content: '提交失败，请稍后重试。',
									showCancel: false,
									confirmText: '确认'
								});
							}
						},
						fail: (res) => {
							uni.hideLoading();
							uni.showModal({
								title: '失败',
								content: '网络异常，请检查网络。',
								showCancel: false,
								confirmText: '确认'
							});
						}
					})
				}
			}
		}
	}
</script>

<style>
	@import url('./feedback.css');
</style>
