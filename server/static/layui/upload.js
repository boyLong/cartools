layui.use(["upload","table"], function(){
    var upload=layui.upload,table=layui.table


    upload.render({
        elem: '#input_wenjuanxing'
        ,url: "/import_wjx"
        ,accept: 'file'
        ,exts:"xlsx|xls"
        ,done: function(res){
            layer.msg(res.msg)

                table.reload('info', {
                          page: {
                            curr: 1 //重新从第 1 页开始
                          }
                          ,where: {
                            key: ""
                       }
                    }, 'data')
          }
    });
    upload.render({
        elem: '#upload_wenjuanxing'
        ,url: "/import_wjx"
        ,accept: 'file'
        ,exts:"xlsx|xls"
        ,done: function(res){
            layer.msg(res.msg)

                table.reload('info', {
                          page: {
                            curr: 1 //重新从第 1 页开始
                          }
                          ,where: {
                            key: ""
                       }
                    }, 'data')
          }
    });
    upload.render({
        elem: '#input_paizheng'
        ,url: "/import_pz"
        ,accept: 'file'
        ,exts:"xlsx|xls"
        ,done: function(res){
            layer.msg(res.msg)

           table.reload('info', {
                          page: {
                            curr: 1 //重新从第 1 页开始
                          }
                          ,where: {
                            key: ""
                       }
                    }, 'data')
          }
    });
    upload.render({
        elem: '#upload_paizheng'
        ,url: "/import_pz"
        ,accept: 'file'
        ,exts:"xlsx|xls"
        ,done: function(res){
            layer.msg(res.msg)

           table.reload('info', {
                          page: {
                            curr: 1 //重新从第 1 页开始
                          }
                          ,where: {
                            key: ""
                       }
                    }, 'data')
          }
    });

 
});

function upperCert(cert,id){
    var $ = layui.jquery;
   if(cert.includes('比亚迪牌')||cert.includes('理念牌')){
      layer.open({
        type: 1
        ,content: '<div style="padding: 20px 100px;"> 注意报销公司 </div>'
        ,btn: '关闭'
        ,btnAlign: 'c' //按钮居中
        ,shade: 0 //不显示遮罩
        ,yes: function(){
             $.ajax({
            type: "post",
            url: "update_cert",
            data: {
                "id": id,
                "CertText":cert
            },

            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                if(data.code===0){
                    $(".certText_"+id)[0].innerHTML=cert
                }

                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
          layer.closeAll();
        }
      })
    }else {
         $.ajax({
            type: "post",
            url: "update_cert",
            data: {
                "id": id,
                "CertText":cert
            },

            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                if(data.code===0){
                    $(".certText_"+id)[0].innerHTML=cert
                }

                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
   }

}


function upperBill(bill,id){
    var $ = layui.jquery;
    $.ajax({
            type: "post",
            url: "update_bill",
            data: {
                "id": id,
                "BillText":bill
            },
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                if(data.code===0){
                    $(".bill_"+id)[0].innerHTML=bill
                }

                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
}


function upperCertManual(id){
    var $ = layui.jquery;

    var form = layui.form;
    form.on('submit(submit)', function(data){
        data = {
              id:id,
              number:data.field.number,
             brand:data.field.brand,
              wpmi:data.field.wpmi,
           engineCode:data.field.engineCode,
            produce:data.field.produce
          }
        if(data.brand.includes('比亚迪牌')||data.brand.includes('理念牌')){
                  layer.open({
        type: 1
        ,content: '<div style="padding: 20px 100px;"> 注意报销公司 </div>'
        ,btn: '关闭'
        ,btnAlign: 'c' //按钮居中
        ,shade: 0 //不显示遮罩
        ,yes: function(){
             $.ajax({
            type: "post",
            url: "update_cert",
            data: data,
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                $(".certText_"+id)[0].innerHTML =data.certText
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })

          layer.closeAll();
        }
      })
        }else {
           $.ajax({
            type: "post",
            url: "update_cert",
            data: data,
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                $(".certText_"+id)[0].innerHTML =data.certText
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
        }

        return false;
      });
    var contet = `<div>
        <form class="layui-form" action="">
           <div class="layui-form-item">
            <label class="layui-form-label">合格证编号</label>
            <div class="layui-input-block">
              <input type="text" name="number" lay-verify="required" style="width: 300px" autocomplete="off" placeholder="" class="layui-input">
            </div>
          </div>
           <div class="layui-form-item">
            <label class="layui-form-label">品牌型号</label>
            <div class="layui-input-block">
              <input type="text" name="brand" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
           <div class="layui-form-item">
            <label class="layui-form-label">车辆识别号</label>
            <div class="layui-input-block">
              <input type="text" name="wpmi" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
           <div class="layui-form-item">
            <label class="layui-form-label">发动机号</label>
            <div class="layui-input-block">
              <input type="text" name="engineCode" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
             </div>
           <div class="layui-form-item">
            <label class="layui-form-label">生产企业名称</label>
            <div class="layui-input-block">
              <input type="text" name="produce" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
             </div>
           <div class="layui-form-item">
            <div class="layui-input-block">
              <button type="submit" class="layui-btn" lay-submit="" lay-filter="submit">立即提交</button>
              <button type="reset" class="layui-btn layui-btn-primary">重置</button>
            </div>
          </div>
         
        </form>
        </div>`
    layer.open({
        title: "合格证",
      type: 1,
      area: ['500px', '400px'],
      content: contet //这里content是一个普通的String
    });
    console.log(id)

}

function del_remarks(o){
      var $ = layui.jquery;

     $.ajax({
            type: "post",
            url: "del_remark",
            data: {"id":o},
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
               location.reload()
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
}

function del_numbers(o){
      var $ = layui.jquery;

     $.ajax({
            type: "post",
            url: "del_number",
            data: {"id":o},
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
               location.reload()
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
}
function add_info(){
    var contet = `<div>
        <form class="layui-form" action="">
           <div class="layui-form-item">
            <label class="layui-form-label">名字</label>
            <div class="layui-input-block">
              <input type="text" name="name"  style="width: 300px" autocomplete="off" placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layui-form-label">公司</label>
            <div class="layui-input-block">
              <input type="text" name="company" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
 
          <div class="layui-form-item">
            <label class="layui-form-label">证件号</label>
            <div class="layui-input-block">
              <input type="text" name="cardNo" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layui-form-label">证件地址</label>
            <div class="layui-input-block">
              <input type="text" name="CardAddress" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>

          <div class="layui-form-item">
            <label class="layui-form-label">代理人</label>
            <div class="layui-input-block">
              <input type="text" name="agent"  autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layui-form-label">手机</label>
            <div class="layui-input-block">
              <input type="text" name="phone"  autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layui-form-label">收铁牌地址</label>
            <div class="layui-input-block">
              <input type="text" name="address"  autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <label class="layui-form-label">销售人员</label>
            <div class="layui-input-block">
              <input type="text" name="saleName" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <div class="layui-input-block">
              <button type="submit" class="layui-btn" lay-submit="" lay-filter="submit_info">立即提交</button>
              <button type="reset" class="layui-btn layui-btn-primary">重置</button>
            </div>
          </div>
        </form>
        </div>`
        layer.open({
        title: "手动录入",
      type: 1,
      area: ['500px', '800px'],
      content: contet //这里content是一个普通的String
    })
        var $ = layui.jquery;

    var form = layui.form;
    form.on('submit(submit_info)', function(data){
        data = {
                name:data.field.name,
                company:data.field.company,
                cardNo:data.field.cardNo,
                CardAddress:data.field.CardAddress,
                agent:data.field.agent,
                phone:data.field.phone,
                address:data.field.address,
                saleName:data.field.saleName,
          }
        $.ajax({
            type: "post",
            url: "add_info",
            data: data,
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
        return false;
      });
}
function upperBillManual(id){
    var $ = layui.jquery;

    var form = layui.form;
    form.on('submit(submit_bill)', function(data){
        data = {
              id:id,
              billCode:data.field.billCode,
             billNumber:data.field.billNumber,
              billDate:data.field.billDate,
          }
        $.ajax({
            type: "post",
            url: "update_bill",
            data: data,
            async:true, // 异步请求
            dataType: 'json', // 返回对象
            success: function(data) {
                $(".bill_"+id)[0].innerHTML =data.billText
                layer.msg(data.msg)
            },
            error: function(data) {
                layer.msg("提交失败")
            }
        })
        return false;
      });
    var contet = `<div>
        <form class="layui-form" action="">
           <div class="layui-form-item">
            <label class="layui-form-label">发票代码</label>
            <div class="layui-input-block">
              <input type="text" name="billCode" lay-verify="required" style="width: 300px" autocomplete="off" placeholder="" class="layui-input">
            </div>
          </div>
           <div class="layui-form-item">
            <label class="layui-form-label">发票号码</label>
            <div class="layui-input-block">
              <input type="text" name="billNumber" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
           <div class="layui-form-item">
            <label class="layui-form-label">开票日期</label>
            <div class="layui-input-block">
              <input type="text" name="billDate" lay-verify="required" autocomplete="off" style="width: 300px"  placeholder="" class="layui-input">
            </div>
          </div>
          <div class="layui-form-item">
            <div class="layui-input-block">
              <button type="submit" class="layui-btn" lay-submit="" lay-filter="submit_bill">立即提交</button>
              <button type="reset" class="layui-btn layui-btn-primary">重置</button>
            </div>
          </div>
 
        </form>
        </div>`
    layer.open({
        title: "发票",
      type: 1,
      area: ['500px', '320px'],
      content: contet //这里content是一个普通的String
    });
    console.log(id)

}
