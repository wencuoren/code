// Author：SuperManito
// Powered by Helloworld
// Date: 2020-04-29
// 自定义配置：
let api = "http://43.138.209.169:55599"; // 面板接口公网地址
let token = "6KiklGExKI4SUvLWfPlA1k6a3raJSJw4"; // 面板接口授权token
let account_limit = 50; // 预设帐号上限，服务器剩余资源为该预设数量减去服务器账号数量

function ExtraAPI() {
  Swal.fire({
    title: "服务器资源管理",
    html:
      '<button id="countCookies" class="el-button el-button--primary is-plain">查询空闲资源</button>&nbsp;&nbsp;' +
      '<button id="submitWSKEY" class="el-button el-button--primary is-plain">提交 WSKEY</button></br>' +
      '<button style="margin: .8em" id="deleteCookie" class="el-button el-button--primary is-plain">删除账号</button>',
    showConfirmButton: false,
    //showCancelButton: true,
    //cancelButtonText: "关闭",
    onBeforeOpen: () => {
      const content = Swal.getContent();
      const $ = content.querySelector.bind(content);

      const ClickcountCookies = $("#countCookies");
      const ClicksubmitWSKEY = $("#submitWSKEY");
      const ClickdeleteCookie = $("#deleteCookie");

      // 查询账号数量
      function countCookies() {
        // 请求接口
        var path = "/openApi/count";
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");
        myHeaders.append("api-token", token);
        var requestOptions = {
          method: "GET",
          redirect: "follow",
          headers: myHeaders,
        };
        return fetch(api + path, requestOptions)
          .then((response) => response.json())
          .then((data) => {
            var code = data.code;
            if (code === 1) {
              var free = account_limit - data.data.cookieCount;
              Swal.fire({
                type: "success",
                title: "查询成功",
                text: "当前服务器还有 " + free + " 个车位",
                showConfirmButton: false,
                timer: 3000,
              });
            } else {
              Swal.fire({
                type: "error",
                title: "查询失败",
                text: JSON.parse(JSON.stringify(data.msg)),
                showConfirmButton: true,
              });
            }
          })
          .catch(() => {
            Swal.fire({
              type: "error",
              title: "未能与服务器建立连接",
              text: "请联系管理员进行处理！",
              showConfirmButton: true,
            });
          });
      }

      // 提交 WSKEY
      function submitWSKEY() {
        Swal.mixin({
          input: "text",
          showCancelButton: true,
          cancelButtonText: "取消",
          progressSteps: ["1", "2", "3"],
        })
          .queue([
            {
              title: "您的京东账户用户名",
              text: "请输入 pt_pin 的值，注意不是昵称是用户名",
              confirmButtonText: "下一步",
            },
            {
              title: "您的 wskey",
              text: "请输入您从京东APP上抓取到的 wskey 的值，注意登录后手动注销或更改密码会导致其失效",
              confirmButtonText: "下一步",
            },
            {
              title: "请输入您的备注",
              confirmButtonText: "确认提交",
              confirmButtonColor: "#28a745",
            },
          ])
          .then((result) => {
            if (result.value) {
              var content = result.value.toString();
              var pt_pin = content.split(",")[0];
              var wskey = content.split(",")[1];
              var remarks = content.split(",")[2];
              var judge_wskey_length =
                wskey.length - 96 == 0 || wskey.length - 118 == 0;

              // 判断提交值是否为空
              if (pt_pin == "") {
                Swal.fire({
                  type: "warning",
                  title: "请不要乱点",
                  showConfirmButton: false,
                  timer: 2000,
                });
              } else if (wskey == "") {
                Swal.fire({
                  type: "warning",
                  title: "请不要乱点",
                  showConfirmButton: false,
                  timer: 2000,
                });
              } else if (judge_wskey_length == false) {
                Swal.fire({
                  type: "error",
                  title: "您的 wskey 格式有误",
                  text: "请验证后重新提交",
                  showConfirmButton: true,
                });
              } else {
                // 请求接口
                var path = "/openApi/addOrUpdateAccount";
                var myHeaders = new Headers();
                myHeaders.append("Content-Type", "application/json");
                myHeaders.append("api-token", token);
                var raw = JSON.stringify({
                  ptPin: encodeURIComponent(pt_pin),
                  wsKey: wskey,
                  remarks: remarks,
                });
                var requestOptions = {
                  method: "POST",
                  headers: myHeaders,
                  body: raw,
                  redirect: "follow",
                };

                return fetch(api + path, requestOptions)
                  .then((response) => response.json())
                  .then((data) => {
                    var code = data.code;
                    if (code === 1) {
                      Swal.fire({
                        type: "success",
                        title: "已提交",
                        showConfirmButton: false,
                        timer: 2000,
                      });
                    } else {
                      Swal.fire({
                        type: "error",
                        title: "提交失败",
                        text: JSON.parse(JSON.stringify(data.msg)),
                        showConfirmButton: true,
                      });
                    }
                  })
                  .catch(() => {
                    Swal.fire({
                      type: "error",
                      title: "未能与服务器建立连接",
                      text: "请联系管理员进行处理！",
                      showConfirmButton: true,
                    });
                  });
              }
            }
          });
      }

      // 删除账号
      function deleteCookie() {
        Swal.fire({
          title: "您的京东账户用户名",
          text: "请输入 pt_pin 的值，注意不是昵称是用户名",
          input: "text",
          confirmButtonText: "确认删除",
          confirmButtonColor: "#dc3545",
          showCancelButton: true,
          cancelButtonText: "取消",
        }).then((result) => {
          if (result.value) {
            // 请求接口
            var path = "/openApi/cookie/delete";
            var myHeaders = new Headers();
            myHeaders.append("Content-Type", "application/json");
            myHeaders.append("api-token", token);
            var deletepin = new Array(encodeURIComponent(result.value));
            var raw = JSON.stringify({
              ptPins: deletepin,
            });
            var requestOptions = {
              method: "POST",
              headers: myHeaders,
              body: raw,
              redirect: "follow",
            };

            return fetch(api + path, requestOptions)
              .then((response) => response.json())
              .then((data) => {
                var code = data.code;
                if (code === 1) {
                  if (data.data.deleteCount === 1) {
                    Swal.fire({
                      type: "success",
                      title: "删除成功",
                      showConfirmButton: false,
                      timer: 2000,
                    });
                  } else {
                    Swal.fire({
                      type: "error",
                      title: "账号不存在",
                      showConfirmButton: true,
                    });
                  }
                } else {
                  Swal.fire({
                    type: "error",
                    title: "删除失败",
                    text: "请联系管理员进行处理！",
                    showConfirmButton: false,
                    timer: 3000,
                  });
                }
              })
              .catch(() => {
                Swal.fire({
                  type: "error",
                  title: "未能与服务器建立连接",
                  text: "请联系管理员进行处理！",
                  showConfirmButton: true,
                });
              });
          } else if (result.value == "") {
            Swal.fire({
              type: "warning",
              title: "请不要乱点",
              showConfirmButton: false,
              timer: 2000,
            });
          }
        });
      }

      ClickcountCookies.addEventListener("click", () => {
        countCookies();
      });
      ClicksubmitWSKEY.addEventListener("click", () => {
        submitWSKEY();
      });
      ClickdeleteCookie.addEventListener("click", () => {
        deleteCookie();
      });
    },
  });
}
