// 所以状态顺序都不变，根据isstar判断增加的状态'
/*
if (row.state == 0) {
	if (row.isDispatch) {
		//车辆调度
		result = '技师未接单';
	} else {
		result = '调度派工中';
	}
	return;
}
if (row.state == 1) {
	if (row.isStar == 0) {
		result = '等待维修';
	} else if (row.isStar == 1) {
		result = '正在维修';
	} else if (row.isStar == 2) {s
		result = '维修暂停';
	} else if (row.isStar == 3) {
		result = '等待增项';
	}
	return;
}
*/
// console.log(res)
function pro(name){
	if(name=="c"){
		
		new Promise((res)=>{
			console.log(res)
		})
		
	}
}
pro("c")