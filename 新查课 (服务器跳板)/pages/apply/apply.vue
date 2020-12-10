<template>
	<view class="container">
		<view @submit="submitApply">
			<view>
				<view class="row blueborder">
					<view class="row baoming applyTitle" style="position: relative;">
						<view class="col-xs-6" style="width: 50%;">
							<h3><i>NEWX</i></h3>
							<h1 style="margin-top: 20upx;"><strong>报名表</strong></h1>
						</view>
						<view style="width: 50%;font-size: 30upx;position: absolute;right: 0;top: 10upx;text-align: center;">
							<view>报名截止时间：</view>
							<view>{{ timePlace.end }}</view>
							<view>活动开始时间：</view>
							<view>{{ timePlace.start }}</view>
							<view>活动地点：</view>
							<view>{{ timePlace.place }}</view>
						</view>
					</view>
					<navigator url="../list/list" class="row howToJoin">
						<view class="col-xs-9">
							<view style="font-size: 25upx;padding: 20upx 0 0 20upx;">如何加入NEWX大学生网络文化工作室呢?</view>
						</view>
						<image style="width: 80upx;height: 80upx" mode="aspectFit" src="../../static/apply/img/pic1.png"></image>
					</navigator>
					<view class="row firsttext">
						<view class="row partTitle">
							<view class="col-xs-5 text-center">
								<h4>基本信息</h4>
							</view>
							<view class="col-xs-7 text-right">
								<h4>///////////////</h4>
							</view>
						</view>
					</view>
					<view class="row">
						<view class="input-group">
							<span class="input-group-addon inputnobor">姓名：</span>
							<input class="form-control" type="text" name="name" v-model="applydata.name" :disabled="cannotChange" />
						</view>
						<view class="input-group radio">
							<span class="input-group-addon inputnobor">性别：</span>
							<radio-group name="allow_adjust" @change="radioChangeGender">
								<radio style="transform:scale(0.7)" :checked="applydata.sex == '男'" value="男" :disabled="cannotChange">男</radio>
								<radio style="transform:scale(0.7)" :checked="applydata.sex == '女'" value="女" :disabled="cannotChange">女</radio>
							</radio-group>
							<!-- <input class="form-control" type="text" name="name" v-model="mes.gender" :disabled="cannotChange" /> -->
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">班级：</span>
							<view class="uni-list-cell-db"><input class="form-control" type="text" name="name" v-model="applydata.class"
								 :disabled="cannotChange" /></view>
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">电子邮箱：</span>
							<input class="form-control" type="email" v-model="applydata.email" placeholder="请输入电子邮箱" placeholder-class="input-placeholder" />
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">电话：</span>
							<input class="form-control" type="text" v-model="applydata.phone" placeholder="请输入手机号" placeholder-class="input-placeholder" />
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">QQ：</span>
							<input class="form-control" type="text" v-model="applydata.qq" placeholder="请输入QQ号" placeholder-class="input-placeholder" />
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">寝室号：</span>
							<input class="form-control" type="text" v-model="applydata.apartment" placeholder="请输入寝室号" placeholder-class="input-placeholder" />
						</view>
						<view class="input-group">
							<span class="input-group-addon inputnobor">志愿1：</span>
							<view class="uni-list-cell-db">
								<picker @change="bindPickerChange1" :value="applydata.option1-1" :range="array" range-key="name">
									<view class="uni-input" style="font-size: 14px;line-height: 25px;">{{ array[applydata.option1-1].name }}</view>
								</picker>
							</view>
							<span class="input-group-addon inputnobor">志愿2：</span>
							<picker @change="bindPickerChange2" :value="applydata.option2-1" :range="array" range-key="name">
								<view class="uni-input" style="font-size: 14px;line-height: 25px;">{{ array[applydata.option2-1].name }}</view>
							</picker>
						</view>
						<view class="input-group ">
							<span class="input-group-addon inputnobor">服从调剂：</span>
							<radio-group name="allow_adjust" @change="radioChange">
								<radio style="transform:scale(0.7)" :checked="applydata.allow_adjust == '1'" value="1">是</radio>
								<radio style="transform:scale(0.7)" :checked="applydata.allow_adjust == '0'" value="0">否</radio>
							</radio-group>
						</view>
					</view>
				</view>
			</view>
			<view class="row" style="display: flex;flex-direction: row;justify-content: space-between;">
				<view class="applyImg" style="padding: 0;padding-left: 1%;">
					<image style="width: 100%;" mode="aspectFit" src="../../static/apply/img/NEWX.png"></image>
					<image style="width: 100%;height: 130upx;" mode="aspectFit" src="../../static/apply/img/pic2.png"></image>
				</view>
				<view class="col-xs-10 applySecond" style="padding-left:0 ;">
					<view class="row blueborder">
						<view class="firsttext partTitle">
							<view class="col-xs-8 " style="font-size: 35upx;">个人简介</view>
							<view class="col-xs-4 text-right">
								<h4>/////////</h4>
							</view>
						</view>
						<textarea style="width: auto;height: 280upx;" maxlength="400" class="form-control" v-model="applydata.profile" rows="5"
						 placeholder="个人简介"></textarea>
					</view>
					<view class="row blueborder">
						<view class="row firsttext partTitle">
							<view class="col-xs-8 " style="font-size: 35upx;">特长及经历</view>
							<view class="col-xs-4 text-right">
								<h4>/////////</h4>
							</view>
						</view>
						<textarea style="width: auto;height: 280upx;" maxlength="400" class="form-control" v-model="applydata.specialty" rows="5"
						 placeholder="特长及经历"></textarea>
					</view>
					<view class="row blueborder">
						<view class="row firsttext partTitle">
							<view class="col-xs-8 " style="font-size: 35upx;">对竞选岗位的认识和看法</view>
							<view class="col-xs-4 text-right">
								<h4>/////////</h4>
							</view>
						</view>
						<textarea style="width: auto;height: 280upx;" maxlength="400" class="form-control" rows="5" v-model="applydata.recognize"
						 placeholder="对竞选岗位的认识和看法"></textarea>
					</view>
					<button @click="submitApply" class="btn btn-default" style="width: 80%;margin: 0 auto;background:#78b9e1;color: white;font-size: 35upx;">
						{{ apply ? '修改' : '提交' }}
					</button>
				</view>
			</view>
		</view>
		<view style="width: 100%;height: 80upx;"></view>
	</view>
</template>

<script>
	var graceChecker = require('./graceChecker.js');
	import Vue from 'vue';
	export default {
		data() {
			return {
				apply: false,
				applydata: {
					uid: '',
					name: '',
					sex: '',
					student_id: '',
					qq: '',
					phone: '',
					apartment: '',
					email: '',
					option1: 1,
					option2: 2,
					allow_adjust: '1',
					profile: '',
					specialty: '',
					recognize: '',
					class: ''
				},
				array: [{
						name: '图文部',
						id: 1
					},
					{
						name: '采风部',
						id: 2
					},
					{
						name: '视频部',
						id: 3
					},
					{
						name: '网站部',
						id: 4
					},
					{
						name: '采编部',
						id: 5
					},
					{
						name: '办公室',
						id: 6
					}
				],
				mes: {},
				cannotChange: false,
				timePlace: {}
			};
		},
		onLoad() {
			uni.request({
				url: Vue.config.baseUrl[0] + 'getapplystatus',
				method: 'POST',
				withCredentials: true,
				header: {
					'content-type': 'application/x-www-form-urlencoded'
				},
				success: res => {
					uni.hideLoading();
					if (res.data.status == 0 || res.data.status == 1) {
						this.timePlace = res.data;
					} else {
						uni.navigateBack();
					}
				},
				fail: res => {
					uni.hideLoading();
					uni.showModal({
						title: '提示',
						content: '请检查网络连接',
						showCancel: false,
						confirmText: '了解'
					});
				}
			});
			this.applydata.student_id = uni.getStorageSync('student_id');
			this.applydata.uid = uni.getStorageSync('user_id' + this.applydata.student_id);
			this.getMessage();
		},
		onBackPress(e) {
			if (e.from == 'navigateBack') {
				return false;
			} else {
				this.setLocalStorage(() => {
					uni.navigateBack();
				});
				return true;
			}
		},
		onShow() {
			this.simpleCheck();
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			getMessage() {
				uni.showLoading({
					title: '加载中……'
				});
				uni.getStorage({
					key: 'my_mes' + this.applydata.student_id,
					success: res => {
						this.mes = res.data;
						this.cannotChange = true;
						
						this.applydata.name = this.mes.user_name;
						this.applydata.sex = this.mes.gender;
						this.applydata.class = this.mes.adminclass_name;
						this.applydata.phone = this.mes.mobile_phone;
						this.applydata.email = this.mes.account_email;
						
						this.checkApply();
					},
					fail: res => {
						Vue.config.cookie = uni.getStorageSync('cookie');
						uni.request({
							url: Vue.config.baseUrl[0] + 'info',
							method: 'POST',
							withCredentials: true,
							header: {
								'content-type': 'application/x-www-form-urlencoded',
								'cookie': Vue.config.cookie
							},
							success: res => {
								if (res.data.code == this.code.success) {
									this.mes = res.data.data;
									this.cannotChange = true;
									
									this.applydata.name = this.mes.user_name;
									this.applydata.sex = this.mes.gender;
									this.applydata.class = this.mes.adminclass_name;
									this.applydata.phone = this.mes.mobile_phone;
									this.applydata.email = this.mes.account_email;
								} else if (res.data.code == this.code.unLogin) {
									// console.log(2)
									// this.error.login();
								} else {
									this.cannotChange = false;
								}
								
								this.checkApply();
							},
							fail: res => {
								this.error.internet();
								this.cannotChange = false;
								
								this.checkApply();
							},
							complete: res => {
								uni.hideLoading();
							}
						});
					}
				});
			},
			checkApply: function() {
				this.uid = uni.getStorageSync('user_id' + this.student_id);
				uni.showLoading({
					title: '加载中',
					mask: true
				});
				uni.request({
					url: Vue.config.baseUrl[3] + 'apply/searchapply?uid=' + this.uid,
					method: 'GET',
					success: res => {
						uni.hideLoading();
						if (res.data.code == this.code.success) {
							this.apply = true;
							this.applydata = res.data.data;
							this.$forceUpdate();
						} else {
							this.apply = false;
							uni.getStorage({
								key: 'apply_data' + this.student_id,
								success: (res) => {
									this.applydata = res.data;
									this.$forceUpdate();
								}
							})
						}
					},
					fail: (res) => {
						this.apply = false;
					}
				});
			},
			radioChange(evt) {
				this.applydata.allow_adjust = evt.detail.value;
			},
			radioChangeGender(e) {
				this.applydata.sex = e.detail.value;
			},
			submitApply: function() {
				let rule = [{
						name: 'name',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写姓名'
					},
					{
						name: 'qq',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写qq'
					},
					{
						name: 'phone',
						checkType: 'phoneon',
						checkRule: '',
						errorMsg: '手机格式错误!!通知将以短信形式发送，请认真填写'
					},
					{
						name: 'apartment',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写宿舍号'
					},
					{
						name: 'email',
						checkType: 'email',
						checkRule: '',
						errorMsg: '邮箱格式错误!!通知将以邮箱形式发送，请认真填写'
					},
					{
						name: 'profile',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写个人简介'
					},
					{
						name: 'specialty',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写特长及经历'
					},
					{
						name: 'recognize',
						checkType: 'notnull',
						checkRule: '',
						errorMsg: '请填写对竞选岗位的认识和看法'
					}
				];
				//进行表单检查
				let checkRes = graceChecker.check(this.applydata, rule);
				let urlStr = '';
				if (this.apply) {
					urlStr = 'apply/editapply';
				} else {
					urlStr = 'apply/addapply';
				}
				if (checkRes) {
					Vue.config.cookie = uni.getStorageSync('cookie');
					uni.request({
						url: Vue.config.baseUrl[3] + urlStr,
						method: 'POST',
						header: {
							'content-type': 'application/x-www-form-urlencoded',
							'cookie': Vue.config.cookie
						},
						data: this.applydata,
						success: res => {
							if (res.data.code == this.code.success) {
								uni.showToast({
									title: '提交成功!',
									icon: 'success'
								});
								let timer1 = setTimeout(function() {
									uni.navigateBack();
								}, 1000);
							} else {
								uni.showToast({
									title: res.data.msg,
									icon: 'none'
								});
							}
						}
					});
				} else {
					uni.showToast({
						title: graceChecker.error,
						icon: 'none'
					});
				}
			},

			bindPickerChange1: function(e) {
				this.applydata.option1 = e.target.value-0+1;
			},
			bindPickerChange2: function(e) {
				this.applydata.option2 = e.target.value-0+1;
			},
			setLocalStorage(fun) {
				uni.setStorage({
					key: 'apply_data' + this.student_id,
					data: this.applydata,
					success: () => {
						fun();
					},
					fail: res => {
						uni.showToast({
							title: '缓存失败'
						});
						fun();
					}
				});
			}
		}
	};
</script>

<style>
	@import url('./apply.css');
</style>
