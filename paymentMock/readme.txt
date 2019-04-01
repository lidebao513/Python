1、首先在应用（新支付系统）的配置文件中把调用第三方的（如资金系统、负债系统）ip或者hosts指向本机ip，默认端口8000。
2、本机配置第三方系统的hosts，如：172.17.2.45 payment.trading.api.pay.ppdaicorp.com。
3、目前支持的mock标签有mock_404、mock_403、mock_500、mock_timeout、mock_all_fail、mock_part_fail、mock_handling、mock_success。
4、接口前不添加mock标签，默认会把应用发来的请求原封不动转给第三方系统，再原封不动把第三方系统的相应内容返回给应用。
5、如示例在views.py中“/payment/PaymentTradeService/CreatePaymentBillBatch”接口前添加mock_404标签，应用在请求这个接口时（对应创建支付单的步骤）会直接返回404，导致创建支付单失败的流程。