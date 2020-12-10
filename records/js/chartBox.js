var chartBox = new Vue({
	el: '#chartBox',
	data: {
		count: 0,
		datas: [],
		dataUse: {
			day: [],

		},
		begin: 0,
		end: 10,
		maxLength: 10
	},
	mounted() {
		if (this.$el.clientHeight > this.$el.clientWidth) {
			this.$el.style.height = (this.$el.clientWidth / 16) * 9 + 'px';
		}
		this.sendRequest();
		this.mekeChart();
	},
	methods: {
		sendRequest() {
			this.$http.get('https://api.jw.huii.top/getrecords').then(res => {
				if (res.body.code == 0) {
					this.count = res.body.count;
					this.datas = res.body.data;
					this.getData();
				} else {
					alert("请检查网络！");
				}
			});
		},
		getData() {
			let tem = {};
			for (let i = 0; i < this.datas.length; i++) {
				if (tem[this.datas[i].date] == null) {
					tem[this.datas[i].date] = 1;
				} else {
					tem[this.datas[i].date]++;
				}
			}
			this.dataUse.day = (Object.keys(tem)).reverse();
			this.dataUse.count = [];
			for (let i = 0; i < this.dataUse.day.length; i++) {
				this.dataUse.count.push(tem[this.dataUse.day[i]]);
			}

			this.end = this.dataUse.day.length;
			this.begin = this.end - 10;
			if (this.begin < 0) {
				this.begin = 0;
			}
			this.maxLength = this.dataUse.day.length;
			this.mekeChart(this.dataUse.day.slice(this.begin, this.end), this.dataUse.count.slice(this.begin, this.end));
		},
		mekeChart(day, count) {
			// 基于准备好的dom，初始化echarts实例
			let chart = echarts.init(this.$refs.chart);

			// 指定图表的配置项和数据
			let chartOption = {
				tooltip: {
					trigger: 'axis',
					formatter: function(params) {
						params = params[0];
						return "日期：" + params.axisValue + "<br>数量：" + params.data;
					},
					axisPointer: {
						animation: false
					}
				},
				xAxis: {
					type: 'category',
					data: day,
					name: '日期',
				},
				yAxis: {
					type: 'value',
					name: '用户数量'
				},
				series: [{
					data: count,
					type: 'line'
				}]
			};

			// 使用刚指定的配置项和数据显示图表。
			chart.setOption(chartOption);
		}
	},
	watch: {
		begin: function() {
			if (this.begin >= this.end) {
				this.end = this.begin + '' - '0' + 1;
			}
			this.mekeChart(this.dataUse.day.slice(this.begin, this.end), this.dataUse.count.slice(this.begin, this.end))
		},
		end: function() {
			if (this.end <= this.begin) {
				this.begin = this.end + '' - '0' - 1;
			}
			this.mekeChart(this.dataUse.day.slice(this.begin, this.end), this.dataUse.count.slice(this.begin, this.end))
		}
	}
})
