# coding=utf-8


# 上一页，下一页之间的页数范围
def get_page_area(page_index, page_total):
    count = 7
    num_area = []
    middle_num = (count / 2) + 1
    if page_index <= middle_num:
        for i in range(1, count + 1):
            if i > page_total:
                break
            num_area.append(i)
    elif page_index >= (page_total - count + middle_num):
        start = 1
        if start > (page_total - count + start):
            start = start - page_total + count
        for i in range(start, count + start):
            index = page_total - count + i
            if index > page_total:
                break
            num_area.append(index)
    else:
        for i in range(1, count + 1):
            index = page_index - middle_num + i
            if index > page_total:
                break
            num_area.append(index)
    return num_area


# 生成分页信息
def build_page_html(page_index, page_total):
    page_area = get_page_area(page_index, page_total)
    html = '<ul style="margin-right: 0px;">'

    if len(page_area) > 0:
        if 1 < page_index:
            html = '%s<li><a href="javascript:void(0)" onclick="do_page(1)" title="转到第一页">First</a></li>' % html
            html = '%s<li><a href="javascript:void(0)" onclick="do_page(%d)" title="转到上一页">Previous</a></li>' % (html, page_index - 1)
        else:
            html = '%s<li class="disabled"><a href="#" title="转到第一页">First</a></li><li class="disabled"><a href="#" title="转到上一页">Previous</a></li>' % html

        for i in page_area:
            if i == page_index:
                html = '%s<li class="active"><a href="#">%d</a></li>' % (html, i)
            else:
                html = '%s<li><a href="javascript:void(0)" onclick="do_page(%d)" title="转到第%d页">%d</a></li>' % (html, i, i, i)

        if page_total > page_index and page_total > 0:
            html = '%s<li><a href="javascript:void(0)" onclick="do_page(%d)" title="转到下一页">Next</a></li>' % (html, page_index + 1)
            html = '%s<li><a href="javascript:void(0)" onclick="do_page(%d)" title="转到最末页">Last</a></li>' % (html, page_total)
        else:
            html = '%s<li class="disabled"><a href="#" title="转到下一页">Next</a></li><li class="disabled"><a href="#" title="转到最末页">Last</a></li>' % html
    else:
        html = '%s<li class="disabled"><a href="#" title="转到第一页">|&laquo;</a></li><li class="disabled"><a href="#" title="转到上一页">Next</a></li>' % html
        html = '%s<li class="disabled"><a href="#" title="转到下一页">&raquo;</a></li><li class="disabled"><a href="#" title="转到最末页">Last</a></li>' % html
    html = '%s</ul>' % html
    return html


if __name__ == '__main__':
    print get_page_area(1, 2)
