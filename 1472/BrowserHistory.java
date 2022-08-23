
import java.util.ArrayList;
import java.util.List;

public class BrowserHistory {

    List<String> list;
    int index;

    public BrowserHistory(String homepage) {
        list = new ArrayList<>();
        list.add(homepage);
        index = 0;
    }

    public void visit(String url) {
        // 可能需要清除最近的历史记录
        if (list.size() -1 > index) {
            list = list.subList(0, index+1);
        }
        // 添加新的记录
        list.add(url);
        index++;
    }

    public String back(int steps) {
        // 需要判断，如果
        if ((index - steps < 0)) {
            index = 0;
            return list.get(index);
        }
        index = index - steps;
        return list.get(index);
    }

    public String forward(int steps) {
        // 需要判断，如果前进的步数超过可前进的步数，则前进到最后一个
        if ((index + steps) >= list.size()) {
            index = list.size()-1;
            return list.get(index);
        }
        index = index + steps;
        return list.get(index);
    }


    public static void main(String[] args) {
        String url ;
        // BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
        // browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google.com"
        
        // browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook.com"
        // browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtube.com"
        // url = browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
        // System.out.println(url);
        // url =  browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
        // System.out.println(url);
        // url = browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
        // System.out.println(url);
        // browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
        // url =  browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
        // System.out.println(url);
        // url = browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
        // System.out.println(url);
        // url = browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"
        // System.out.println(url);


//         ["BrowserHistory","visit","back","back","forward","forward","visit","visit","back"]
// [["zav.com"],["kni.com"],[7],[7],[5],[1],["pwrrbnw.com"],["mosohif.com"],[9]]
        BrowserHistory browserHistory = new BrowserHistory("zav.com");
        browserHistory.visit("kni.com");
        browserHistory.back(7);
        browserHistory.back(7);
        browserHistory.forward(5);
        browserHistory.forward(1);
        browserHistory.visit("pwrrbnw.com");
        browserHistory.visit("mosohif.com");
        browserHistory.back(9);
    }
}