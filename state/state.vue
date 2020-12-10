<template>
	<view id="state">
		<view id="summary">
			<view>
				<view style="color: #000000;">当前状态：</view>
				<view>{{ stataWord }}</view>
			</view>
			<view style="margin-top: 4%;">
				<view style="color: #000000;">处理部门：</view>
				<view>{{ deWord }}</view>
			</view>
			<view style="margin-top: 4%;">
				<view style="color: #000000;">通知：</view>
				<view>{{ notice }}</view>
			</view>
		</view>
		<view id="canvas">
			<view v-if="code==-1" class="begin" @click="goToApply">前往填写报名表</view>
			<view v-else class="begin" @click="goToApply">前往修改报名表</view>
			<view class="lineCanvas" ref="lineCanvas1">
				<canvas style="width: 100%; height: 100%;" canvas-id="stateLine1"></canvas>
			</view>
			<view class="cricleCanvas" ref="cricleCanvas1">
				<view class="criNum rightNum" v-show="num_1==1">1
					<view class="criWord rightWord" v-if="code==0">报名表提交成功！</view>
				</view>
				<canvas style="width: 100%; height: 100%;" canvas-id="stateCricle1"></canvas>
			</view>
			<view class="cricleCanvas" ref="cricleCanvas2">
				<view class="criNum leftNum" v-show="num_2==1">2
					<view class="criWord leftWord" v-if="data.status==1">一面时间：<br>国庆前(具体时间待定)</view>
					<view class="criWord leftWord" v-else-if="data.status==-1">对不起，一面失败！</view>
					<view class="criWord leftWord" v-else-if="data.status==2||data.status==3||data.status==-2">恭喜，一面通过！</view>
				</view>
				<canvas style="width: 100%; height: 100%;" canvas-id="stateCricle2"></canvas>
			</view>
			<view class="lineCanvas" style="transform: translateY(-100%);width: 60%;" ref="lineCanvas2">
				<canvas style="width: 100%; height: 100%;" canvas-id="stateLine2"></canvas>
			</view>
			<view class="lineCanvas" style="transform: translateY(-100%);width: 59%;" ref="lineCanvas3">
				<view v-show="num_3==1" class="lineWord" v-if="data.status==2||data.status==-2||data.status==3">处理部门：{{ deWordOnLine_1 }}</view>
				<canvas style="width: 100%; height: 100%;" canvas-id="stateLine3"></canvas>
			</view>
			<view class="cricleCanvas" ref="cricleCanvas3">
				<view class="criNum rightNum" v-show="num_4==1">3
					<view class="criWord rightWord" v-if="data.status==2">二面时间：<br>国庆后(具体时间待定)</view>
					<view class="criWord rightWord" v-else-if="data.status==-2">对不起，二面失败！</view>
					<view class="criWord rightWord" v-else-if="data.status==3">恭喜，二面通过！</view>
				</view>
				<canvas style="width: 100%; height: 100%;" canvas-id="stateCricle3"></canvas>
			</view>
			<view class="lineCanvas" id="lineLast" style="transform: translateY(-100%);" ref="lineCanvas4">
				<view class="overWord" v-if="data.status==3&&num_5==1">恭喜您已经被录取！</view>
				<canvas style="width: 100%; height: 100%;" canvas-id="stateLine4"></canvas>
			</view>
		</view>
	</view>
</template>

<script>
	import Vue from 'vue'
	export default {
		data() {
			return {
				code: null,
				data: {
					addmit_department: null,
					status: null
				},
				num_1: 0,
				num_2: 0,
				num_3: 0,
				num_4: 0,
				num_5: 0
			}
		},
		onShareAppMessage: function() {
			return this.shareFunction();
		},
		methods: {
			goToApply() {
				uni.switchTab({
					url: "../apply/apply"
				});
			},
			makeLine(name, sx, sy, ex, ey, time, scolor, ecolor) {
				var ctx = uni.createCanvasContext(name);
				var colorend = this.$refs.lineCanvas2.$el.clientWidth;
				var gradient = ctx.createLinearGradient(0, 0, colorend, 0);
				gradient.addColorStop("0", scolor);
				gradient.addColorStop("1", ecolor);
				// gradient.addColorStop("1.0", "#1574a4");

				var nx = sx;
				var ny = sy;
				if (time != 0) {
					var stepx = (ex - sx) / (time / 10);
					var stepy = (ey - sy) / (time / 10);
				} else {
					var stepx = (ex - sx);
					var stepy = (ey - sy);
				}
				// console.log(stepx)
				var that = this;
				var MLSet = setInterval(function() {
					nx = nx + stepx;
					ny = ny + stepy;
					// ctx.setStrokeStyle(scolor);
					ctx.strokeStyle = gradient;
					ctx.lineWidth = that.$refs.lineCanvas1.$el.clientHeight;
					ctx.lineCap = "round";
					ctx.moveTo(sx, sy);
					ctx.lineTo(nx, ny);
					ctx.stroke();
					ctx.draw();
					if ((nx >= ex && ny >= ey && ex > sx) || (nx <= ex && ny <= ey && ex < sx)) {
						clearInterval(MLSet);
					}
				}, 10)
			},
			makeCircle(name, x, y, r, sa, ea, dir, time, scolor, ecolor) {
				var ctx = uni.createCanvasContext(name);
				var colorend = this.$refs.cricleCanvas1.$el.clientWidth;
				var gradient = ctx.createLinearGradient(0, 0, colorend, colorend * 2);
				gradient.addColorStop("0", scolor);
				gradient.addColorStop("1", ecolor);

				var na = sa;
				if (time != 0) {
					var stepa = (ea - sa) / (time / 10);
				} else {
					var stepa = (ea - sa);
				}
				var that = this;
				var MCSet = setInterval(function() {
					na = na + stepa;
					ctx.strokeStyle = gradient;
					ctx.lineWidth = that.$refs.lineCanvas1.$el.clientHeight;
					ctx.lineCap = "round";
					ctx.arc(x, y, r, sa * Math.PI, na * Math.PI, dir);
					ctx.stroke();
					ctx.draw();
					if ((na >= ea && ea > sa) || (na <= ea && ea < sa)) {
						clearInterval(MCSet);
					}
				}, 10)
			}
		},
		mounted() {
			this.$refs.cricleCanvas1.$el.style.height = this.$refs.cricleCanvas1.$el.clientWidth * 2 + 'px';
			// this.$refs.cricleLine1.$el.style.height = this.$refs.cricleCanvas1.$el.clientWidth + 'px';
			this.$refs.cricleCanvas2.$el.style.height = this.$refs.cricleCanvas2.$el.clientWidth * 2 + 'px';
			// this.$refs.cricleLine2.$el.style.height = this.$refs.cricleCanvas1.$el.clientWidth + 'px';
			this.$refs.cricleCanvas2.$el.style.marginTop = -this.$refs.lineCanvas2.$el.clientHeight + 'px';

			this.$refs.lineCanvas3.$el.style.marginLeft = this.$refs.cricleCanvas2.$el.clientWidth + 'px';
			this.$refs.cricleCanvas3.$el.style.height = this.$refs.cricleCanvas3.$el.clientWidth * 2 + 'px';
			this.$refs.cricleCanvas3.$el.style.marginTop = -this.$refs.lineCanvas3.$el.clientHeight + 'px';

			uni.showLoading({
				title: '加载中'
			});
			var uid = uni.getStorageSync('user_id');
			uni.request({
				url: Vue.config.baseUrl + 'apply/status?uid=' + uid,
				method: 'GET',
				success: (res) => {
					// if (res.code == 0) {} else if (res.code == -1) {}
					// console.log(res)
					this.code = res.data.code;
					this.data = res.data.data;
					uni.hideLoading();
					var len = this.$refs.lineCanvas1.$el.clientWidth;
					var lineW = this.$refs.lineCanvas1.$el.clientHeight;
					if (this.code == 0 && this.data.status == 3) {
						var colorArr = ['#ecfbff', '#c4e9fe', '#c4e9fe', '#a5ddfd', '#95cae6', '#afe1fd', '#c4e9fe', '#1574a4',
							'#217caa', '#2b80ae', '#257fac', '#6d89c3', '#5d87be', '#5d87be'
						];
					} else if (this.code == 0 && (this.data.status == -2 || this.data.status == 2)) {
						var colorArr = ['#ecfbff', '#c4e9fe', '#c4e9fe', '#a5ddfd', '#95cae6', '#afe1fd', '#c4e9fe', '#1574a4',
							'#217caa', '#2b80ae', '#257fac', 'gray', 'gray', '#67808c'
						];
					} else if (this.code == 0 && (this.data.status == -1 || this.data.status == 1)) {
						var colorArr = ['#ecfbff', '#c4e9fe', '#c4e9fe', '#a5ddfd', '#b1ccdc', '#afe1fd', '#c4e9fe', 'gray', '#848788',
							'gray', 'gray', 'gray', 'gray', 'gray'
						];
					} else if (this.code == -1) {
						var colorArr = ['gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray',
							'gray', 'gray'
						];
					}
					this.makeLine('stateLine1', 0, lineW / 2, len, lineW / 2, 200, colorArr[0], colorArr[1])

					var me = this;
					var y = this.$refs.cricleCanvas1.$el.clientWidth;
					setTimeout(function() {
						me.makeCircle('stateCricle1', 0, y, y - lineW / 2, -0.5, 0.5, false, 200, colorArr[2], colorArr[3]);
						me.num_1 = 1;
					}, 300)
					setTimeout(function() {
						var sx = me.$refs.lineCanvas2.$el.clientWidth;
						var sy = me.$refs.lineCanvas2.$el.clientHeight - lineW / 2;
						me.makeLine('stateLine2', sx, sy, 0, sy, 200, colorArr[4], colorArr[5])
					}, 600)
					setTimeout(function() {
						var x = me.$refs.cricleCanvas2.$el.clientWidth;
						me.makeCircle('stateCricle2', x, y, y - lineW / 2, -0.5, -1.5, true, 200, colorArr[6], colorArr[7]);
						me.num_2 = 1;
					}, 900)
					setTimeout(function() {
						var ex = me.$refs.lineCanvas2.$el.clientWidth;
						var sy = me.$refs.lineCanvas2.$el.clientHeight - lineW / 2;
						me.makeLine('stateLine3', 0, sy, ex, sy, 200, colorArr[8], colorArr[9])
						me.num_3 = 1;
					}, 1200)
					setTimeout(function() {
						var x = me.$refs.cricleCanvas2.$el.clientWidth;
						me.makeCircle('stateCricle3', 0, y, y - lineW / 2, -0.5, 0.5, false, 200, colorArr[10], colorArr[11]);
						me.num_4 = 1;
					}, 1500)
					setTimeout(function() {
						var ex = me.$refs.lineCanvas2.$el.clientWidth;
						var sy = me.$refs.lineCanvas2.$el.clientHeight - lineW / 2;
						me.makeLine('stateLine4', len, lineW / 2, len / 20, lineW / 2, 200, colorArr[12], colorArr[13])
						me.num_5 = 1;
					}, 1800)

				}
			})

		},
		onReady() {},
		computed: {
			'stataWord': function() {
				if (this.code == 0 && this.data.status == 1) {
					return '报名表已提交(可修改)，请准备一面！';
				} else if (this.code == 0 && (this.data.status == -1 || this.data.status == -2)) {
					return '对不起，您未通过面试！感谢您对我们的支持！';
				} else if (this.code == 0 && this.data.status == 2) {
					return '一面通过，请准备二面！';
				} else if (this.code == 0 && this.data.status == 3) {
					return '恭喜您，您已经被录取！请等待第一次全体会议！';
				} else if (this.code == -1) {
					return '请填写报名表！'
				}
			},
			'deWord': function() {
				if (this.code == 0 && this.data.status == 1) {
					return '工作室统一处理中';
				} else if (this.code == 0 && (this.data.status == -1 || this.data.status == -2)) {
					return '----------';
				} else if (this.code == 0 && this.data.status == 2) {
					var word = '';
					switch (parseInt(this.data.addmit_department)) {
						case 1:
							word = '图文部受理中';
							break;
						case 2:
							word = '采风部受理中';
							break;
						case 3:
							word = '视频部受理中';
							break;
						case 4:
							word = '网站部受理中';
							break;
						default:
							word = '系统错误！';
							break;
					}
					return word;
				} else if (this.code == 0 && this.data.status == 3) {
					var word = '';
					switch (parseInt(this.data.addmit_department)) {
						case 1:
							word = '图文部录取';
							break;
						case 2:
							word = '采风部录取';
							break;
						case 3:
							word = '视频部录取';
							break;
						case 4:
							word = '网站部录取';
							break;
						case 5:
							word = '采编部录取';
							break;
						case 6:
							word = '办公室录取';
						default:
							word = '系统错误！';
							break;
					}
					return word;
				} else if (this.code == -1) {
					return '----------'
				}
			},
			'deWordOnLine_1': function() {
				if (this.code == 0 && (this.data.status == 2 || this.data.status == 3 || this.data.status == -2)) {
					var word = '';
					switch (parseInt(this.data.addmit_department)) {
						case 1:
							word = '图文部';
							break;
						case 2:
							word = '采风部';
							break;
						case 3:
							word = '视频部';
							break;
						case 4:
							word = '网站部';
							break;
						case 5:
							word = '采编部';
							break;
						case 6:
							word = '办公室';
							break;
						default:
							word = '系统错误！';
							break;
					}
					return word;
				}
			},
			'notice': function() {
				if (this.code == -1) {
					return '将在达到报名限额后关闭报名通道，请尽快填写报名表！'
				} else if (this.code == 0 && this.data.status == 1) {
					return '第一次面试具体时间待定，地点待定；请加入NEWX迎新群621496212，及时关注面试动态，并做好准备！'
				} else if (this.code == 0 && this.data.status == 2) {
					return '第二次面试具体时间待定，地点待定；请添加各部门指定二面群，及时关注面试动态，并做好准备！'
				} else if (this.code == 0 && this.data.status == 3) {
					return '恭喜您通过了面试！第一次全体会议定于二面后(时间待定)开始，地点待定，请及时关注会议动态！'
				} else {
					return '本次面试已经结束，感谢您对我们的支持。在面试中您表现优异，但综合考虑您目前并不适合在工作室工作，请不要灰心，祝您早日找到适合自己的组织！'
				}
			}
		}
	}
</script>

<style>
	#state {
		width: 100%;
		/* padding: 5%; */
		background-color: #f9f9f9;
		font-size: 0;
	}

	#stateTitle {
		width: 100%;
		height: 80upx;
		padding: 40upx 0 0 40upx;
		display: flex;
		flex-direction: row;
		background-color: white;
		position: fixed;
		z-index: 4;
		top: 0;
		left: 0;
		border-bottom: #ececec 2px solid;
		color: #a8a8a8;
	}

	#stateTitle>view {
		font-size: 40upx;
		margin: 5upx 0 0 210upx;
	}

	#summary {
		width: 80%;
		/* height: 200upx; */
		margin: 4% auto 0 auto;
		padding: 5% 4%;
		background-color: white;
		border-radius: 20upx;
		box-shadow: 0 5upx 10upx #a8a8a8;
		font-size: 35upx;
		color: #737373;
		text-align: center;
	}

	#canvas {
		width: 80%;
		margin: 20% auto;
		/* padding: 20% 0; */
		position: relative;
	}

	.lineCanvas {
		width: 80%;
		height: 40upx;
		/* margin: 180upx 80upx; */
		/* background-color: #8DC63F; */
		display: inline-block;
		vertical-align: top;
		position: relative;
	}

	.cricleCanvas {
		width: 20%;
		height: 800upx;
		/* background-color: red; */
		display: inline-block;
		vertical-align: top;
		position: relative;
	}

	.begin {
		position: absolute;
		top: 0;
		left: 0;
		font-size: 30upx;
		z-index: 2;
		width: 120upx;
		text-align: center;
		background-color: white;
		padding: 2%;
		box-shadow: 0 -5upx 10upx #a8a8a8 inset;
		border-radius: 20upx;
		transform: rotate(-20deg) translateY(-30%);
	}

	.criNum {
		position: absolute;
		z-index: 2;
		width: 50upx;
		height: 50upx;
		border-radius: 80upx;
		/* border: #000000 2px solid; */
		background-color: white;
		font-size: 40upx;
		font-weight: 900;
		text-align: center;
		top: 50%;
		transform: translateY(-50%);
		box-shadow: 0 -5upx 15upx #a8a8a8 inset;
	}

	.rightNum {
		left: 50%;
	}

	.leftNum {
		left: 10%;
	}

	.criWord {
		position: absolute;
		z-index: 2;
		background-color: white;
		font-size: 30upx;
		box-shadow: 0 -5upx 15upx #a8a8a8 inset;
		width: 300upx;
		color: #a8a8a8;
		font-weight: normal;
		top: 50%;
		transform: translateY(-50%);
	}

	.rightWord {
		border-top-right-radius: 20upx;
		border-bottom-right-radius: 20upx;
		border-top-left-radius: 5upx;
		border-bottom-left-radius: 5upx;
		right: 100%;
	}

	.leftWord {
		border-top-right-radius: 5upx;
		border-bottom-right-radius: 5upx;
		border-top-left-radius: 20upx;
		border-bottom-left-radius: 20upx;
		left: 100%;
	}

	.lineWord {
		position: absolute;
		z-index: 2;
		/* background-color: white; */
		font-size: 30upx;
		box-shadow: 0 -5upx 15upx #a8a8a8 inset;
		width: 300upx;
		color: white;
		text-align: center;
		/* transform: rotate(-10deg); */
		left: 50%;
		transform: translateX(-50%);
	}

	.overWord {
		position: absolute;
		top: 0;
		left: 0;
		font-size: 30upx;
		z-index: 2;
		width: 120upx;
		text-align: center;
		background-color: white;
		padding: 2%;
		box-shadow: 0 -5upx 10upx #a8a8a8 inset;
		border-radius: 20upx;
		transform: rotate(20deg) translateY(-30%);
	}
</style>
