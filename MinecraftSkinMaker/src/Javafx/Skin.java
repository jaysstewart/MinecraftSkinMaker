package Javafx;

import java.io.File;
//skin object
public class Skin {
    //Location of imgs
    File head;
    File body;
    File lArm;
    File rArm;
    File lLeg;
    File rLeg;

    //consturctor
    Skin (File head, File body, File lArm, File rArm, File lLeg, File rLeg) {
        this.head = head;
        this.body = body;
        this.lArm = lArm;
        this.rArm = rArm;
        this.lLeg = lLeg;
        this.rLeg = rLeg;
    }

    //getters & setters

    public File getHead() {
        return head;
    }

    public void setHead(File head) {
        this.head = head;
    }

    public File getBody() {
        return body;
    }

    public void setBody(File body) {
        this.body = body;
    }

    public File getlArm() {
        return lArm;
    }

    public void setlArm(File lArm) {
        this.lArm = lArm;
    }

    public File getrArm() {
        return rArm;
    }

    public void setrArm(File rArm) {
        this.rArm = rArm;
    }

    public File getlLeg() {
        return lLeg;
    }

    public void setlLeg(File lLeg) {
        this.lLeg = lLeg;
    }

    public File getrLeg() {
        return rLeg;
    }

    public void setrLeg(File rLeg) {
        this.rLeg = rLeg;
    }
}
