#生成问卷
import sys
sys.path.append("d:\\anaconda\\lib\\site-packages")
#解决dash库文件不在系统路径内，在cmd中输入pip show dash来展示dash所在位置并添加到这里
import json
import re
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

#编写dash页面布局
app = dash.Dash(__name__)#链接到样式表
app.layout = html.Div(
    dbc.Container(
        [
            html.H1('学生宿舍需求问卷'),
            html.Br(),

            html.P('1.姓名：'),
            html.Hr(),
            dbc.Input(#填空
                id='name',
                placeholder='姓名',
                autoComplete='off',
                style={
                    'width': '400px'
                }
            ),
            html.Hr(),

            html.P('2.学号：'),
            html.Hr(),
            dbc.Input(#填空
                id='num',
                placeholder='学号',
                autoComplete='off',
                style={
                    'width': '400px'
                }
            ),
            html.Hr(),

            html.P('3.性别：'),
            html.Hr(),
            dbc.RadioItems(#单选
                id='gender',
                inline=True,
                options=[
                    {'label': '男', 'value': 'M'},
                    {'label': '女', 'value': 'F'}
                ]
            ),
            html.Br(),

            html.P('4.晚上睡觉时间：'),
            html.Hr(),
            dbc.RadioItems(#单选
                id='time',
                inline=True,
                options=[
                    {'label': '10:00~11:00', 'value': '0'},
                    {'label': '11:00~12:00', 'value': '1'},
                    {'label': '12:00~1:00', 'value': '2'},
                ]
            ),
            html.Br(),

            html.P('5.您介意舍友哪些习惯（多选）：'),
            html.Hr(),
            dbc.Checklist(#多选
                id='habits',
                inline=True,
                options=[
                    {'label': '睡觉打呼噜', 'value': '0'},
                    {'label': '大声说话', 'value': '1'},
                    {'label': '不爱卫生', 'value': '2'}
                ]
            ),
            html.Br(),

            dbc.Button(
                '点击提交',
                id='submit'
            ),

            html.P(id='user-info')

        ],
        style={
            'margin-top': '50px',
            'margin-bottom': '200px'
        }
    )
)
#编写回调函数
@app.callback(
    Output('user-info', 'children'),
    Input('submit', 'n_clicks'),
    [
        State('name', 'value'),
        State('num', 'value'),
        State('gender', 'value'),
        State('time', 'value'),
        State('habits', 'value')
    ],
    prevent_initial_call=True
)
def fetch_info(n_clicks, name, num, gender, time, habits):
    if all([name, num, gender, time, habits]):
        f=open("all.txt",'a')
        f.write(str(name)+str(num)+str(gender)+str(time)+str(habits))#list转换为str
        f.close()
        f=open("gender.txt",'a')
        f.write(gender)
        f.close()
        f=open("time.txt",'a')
        f.write(time)
        f.close()
        f=open("habits.txt",'a')
        f.write(str(habits))
        f.close()
        return 'submit success！'
    else:
        return '信息未填写完全！'

@app.callback(
    [Output('num', 'valid'),
     Output('num', 'invalid')],
    Input('num', 'value'),
    prevent_initial_call=True
)
def check_num(value):
    try:
        if re.findall('\d+', value)[0] == value and len(value) == 11:
            return True, False
    except:
        pass
    return False, True

#启动
if __name__ == '__main__':
    app.run_server(debug=True)